
import numpy as np
import sounddevice as sd
import whisper
from collections import deque
import keyboard
import torch

# ==== Settings / Настройки ====
SAMPLE_RATE = 16000  # Do not change, sound quality to send to AI / Не изменяй, качество звука для передачи в ИИ
CHUNK_DURATION = 0.3  # Do not change, Chunk duration in seconds / Длительность фрагмента в секундах
WHISPER_MODEL = 'small'  # tiny / base / small / medium / large  Whisper model being used / Используемая модель Whisper   
#C:\Users\_USER_\.cache\whisper  Model will be loaded  here 
THRESHOLD = 0.015  # Sound sensitivity / Чувствительность к звуку

SILENCE_DURATION = 0.3  # Silence duration before stopping / Длительность тишины перед остановкой
PRE_RECORD_SECONDS = 1.0  # Length of the "past" sound buffer / Длина буфера "прошлого" звука
LANGUAGE = 'en'  # Processing language / Язык обработки



# 🔒 Hotkeys / Горячие фразы
hotkey0 = ""  
hotkey1 = "healing"
hotkey2 = ""
hotkey3 = "fireball"
hotkey4 = ""
hotkey5 = ""
hotkey6 = ""
hotkey7 = ""
hotkey8 = ""
hotkey9 = ""
stop_word = "стоп"  
stop_word2 = "stop"

# === Device identification / Определение устройства ===

if torch.cuda.is_available():
    DEVICE = "cuda"
    FP16 = True
    print("⚡ Using GPU (CUDA) /  Используем GPU (CUDA)")
else:
    DEVICE = "cpu"
    FP16 = False
    print("🖥 Using CPU / Используем CPU")

print("CUDA  avalible / доступна:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Device qty / Количество устройств:", torch.cuda.device_count())
    print("Device name / Имя устройства:", torch.cuda.get_device_name(0))


# === Model Loading === → # === Загрузка модели ===

print("🧠 / Loading Whisper model / Загружаем модель Whisper...")
model = whisper.load_model(f"{WHISPER_MODEL}", device=DEVICE)

# === Sending Keystrokes === → # === Отправка клавиш ===
def send_hotkey(key):
    if 0 <= key <= 9:
        try:
            keyboard.send(str(key))  # обычная цифра
        except ValueError as e:
            print(f"❌ Error while sending / Ошибка при отправке: {e}")
    else:
        print("❌ Error: key out of range 0–9  / Ошибка: ключ вне диапазона 0–9")

# === Command Processing === → # === Обработка команды ===
def handle_command(text):
    text = text.strip().lower()
    if stop_word in text or stop_word2 in text:
        print("🚩 Command 'stop' received — terminating. / Получена команда 'стоп' — завершение.")
        return False

    for i in range(10):
        hotkey = globals().get(f"hotkey{i}")
        if hotkey and hotkey in text:
            print(f"🎯 Hotkey triggered / Сработал hotkey{i} ('{hotkey}') — sending / отправляем {i}")
            send_hotkey(i)
            return True

    print("🤷 Command not recognized / Команда не распознана")
    return True

# === Проверка громкости ===
def is_loud(data, threshold):
    return np.max(np.abs(data)) > threshold

# === Основной цикл прослушивания ===
def listen_loop():
    print("🎧 Starting infinite listening loop...  / Начинаем бесконечный цикл прослушивания...")

    buffer_chunks = int(PRE_RECORD_SECONDS / CHUNK_DURATION)
    pre_buffer = deque(maxlen=buffer_chunks)

    device_info = sd.query_devices(kind='input')
    input_channels = device_info['max_input_channels']
    print(f"🎚️ Detected input channels / Обнаружено входных каналов: {input_channels}")

    while True:
        print("🔎 Waiting for sound... / Ожидание звука...")

        recording = []
        silence_time = 0.0
        recording_started = False
        stop_stream = False

        def callback(indata, frames, time_info, status):
            nonlocal recording, silence_time, recording_started, stop_stream

            volume = np.linalg.norm(indata)
            print(f"🔊 MIC Volume / Громкость: {volume:.5f}")

            # Преобразуем в моно, если нужно
            if indata.shape[1] > 1:
                mono_data = np.mean(indata, axis=1, keepdims=True)
            else:
                mono_data = indata

            pre_buffer.append(mono_data.copy())

            if is_loud(mono_data, THRESHOLD):
                if not recording_started:
                    print("🔴 Sound detected, starting recording... / Обнаружен звук, начинаем запись...")
                    recording.extend(list(pre_buffer))
                    recording_started = True
                silence_time = 0.0
                recording.append(mono_data.copy())
            elif recording_started:
                silence_time += CHUNK_DURATION
                print(f"🟡 Silence / Тишина {silence_time:.2f} сек...")
                recording.append(mono_data.copy())
                if silence_time >= SILENCE_DURATION:
                    print("⏹️ Recording finished / Запись завершена")
                    stop_stream = True

        with sd.InputStream(callback=callback,
                            channels=input_channels,
                            samplerate=SAMPLE_RATE,
                            blocksize=int(SAMPLE_RATE * CHUNK_DURATION)):
            while not stop_stream:
                sd.sleep(int(CHUNK_DURATION * 1000))

        if not recording:
            print("🟡 Sound not detected — nothing recognized / Звук не был обнаружен — ничего не распознано")
            continue

        print(f"✅ Processing / Обработка {len(recording)} cunks / чанков...")
        full = np.concatenate(recording).flatten().astype(np.float32)

        try:
            result = model.transcribe(full, language=LANGUAGE, fp16=FP16)
            print("📝 Recognized text / Распознанный текст:", result["text"])
            if not handle_command(result["text"]):
                break
        except Exception as e:
            print(f"❌ Error during recognition / Ошибка при распознавании: {e}")

# === Точка входа ===
if __name__ == "__main__":
    listen_loop()
