import numpy as np
import sounddevice as sd
import whisper
from collections import deque
import keyboard
import torch
import os
import sys

# ==== Settings / Настройки ====
SAMPLE_RATE = 16000  # Do not change / Не изменяй
CHUNK_DURATION = 0.3  # Do not change / Не изменяй
WHISPER_MODEL = 'small'  # tiny / base / small / medium / large
THRESHOLD = 0.015  # Sound sensitivity / Чувствительность
SILENCE_DURATION = 0.3  # Silence stop delay / Задержка остановки
PRE_RECORD_SECONDS = 1.0  # Audio buffer / Буфер
LANGUAGE = 'en'  # Language / Язык

# === Hotwords / Горячие слова ===
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

# === Logging / Логирование ===
# log_buffer = deque(maxlen=100)

log_history = []

def log(msg):
    global log_history
    line = msg if isinstance(msg, str) else str(msg)
    log_history.append(line)
    if len(log_history) > 100:
        del log_history[:-50]  # Храним только последние 50 / Last 50 prints

    # Сдфк ыскуут / Очистка экрана
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Печатаем последние строки
    for l in log_history[-50:]:
        print(l)


# === Send hotkey / Отправка горячей клавиши ===
def send_hotkey(key):
    if 0 <= key <= 9:
        try:
            keyboard.send(str(key))
        except ValueError as e:
            log(f"❌ Error while sending / Ошибка при отправке: {e}")
    else:
        log("❌ Error: key out of range 0–9 / Ошибка: ключ вне диапазона 0–9")

# === Handle command / Обработка команды ===
def handle_command(text):
    text = text.strip().lower()
    if stop_word in text or stop_word2 in text:
        log("🚩 Command 'stop' received / Получена команда 'стоп' — завершение.")
        return False

    for i in range(10):
        hotkey = globals().get(f"hotkey{i}")
        if hotkey and hotkey in text:
            log(f"🎯 Hotkey{i} triggered ('{hotkey}') / Сработал hotkey{i} ('{hotkey}') — отправляем {i}")
            send_hotkey(i)
            return True

    log("🤷 Command not recognized / Команда не распознана")
    return True

# === Volume check / Проверка громкости ===
def is_loud(data, threshold):
    return np.max(np.abs(data)) > threshold

# === Main listen loop / Основной цикл прослушивания ===
def listen_loop():
    log("🎧 Starting infinite listening loop / Начинаем бесконечный цикл прослушивания...")

    buffer_chunks = int(PRE_RECORD_SECONDS / CHUNK_DURATION)
    pre_buffer = deque(maxlen=buffer_chunks)

    device_info = sd.query_devices(kind='input')
    input_channels = device_info['max_input_channels']
    log(f"🎚️ Detected input channels: {input_channels} / Обнаружено входных каналов: {input_channels}")

    while True:
        log("🔎 Waiting for sound... / Ожидание звука...")

        recording = []
        silence_time = 0.0
        recording_started = False
        stop_stream = False

        def callback(indata, frames, time_info, status):
            nonlocal recording, silence_time, recording_started, stop_stream

            volume = np.linalg.norm(indata)
            log("🔊 MIC Volume / Громкость: {:.5f}".format(volume))

            if indata.shape[1] > 1:
                mono_data = np.mean(indata, axis=1, keepdims=True)
            else:
                mono_data = indata

            pre_buffer.append(mono_data.copy())

            if is_loud(mono_data, THRESHOLD):
                if not recording_started:
                    log("🔴 Sound detected / Обнаружен звук — начинаем запись...")
                    recording.extend(list(pre_buffer))
                    recording_started = True
                silence_time = 0.0
                recording.append(mono_data.copy())
            elif recording_started:
                silence_time += CHUNK_DURATION
                log(f"🟡 Silence {silence_time:.2f} sec... / Тишина {silence_time:.2f} сек...")
                recording.append(mono_data.copy())
                if silence_time >= SILENCE_DURATION:
                    log("⏹️ Recording finished / Запись завершена")
                    stop_stream = True

        with sd.InputStream(callback=callback,
                            channels=input_channels,
                            samplerate=SAMPLE_RATE,
                            blocksize=int(SAMPLE_RATE * CHUNK_DURATION)):
            while not stop_stream:
                sd.sleep(int(CHUNK_DURATION * 1000))

        if not recording:
            log("🟡 No sound detected / Звук не был обнаружен")
            continue

        log(f"✅ Processing {len(recording)} chunks / Обработка {len(recording)} чанков...")
        full = np.concatenate(recording).flatten().astype(np.float32)

        try:
            result = model.transcribe(full, language=LANGUAGE, fp16=FP16)
            log("📝 Recognized text / Распознанный текст: " + result["text"])
            if not handle_command(result["text"]):
                break
        except Exception as e:
            log(f"❌ Error during recognition / Ошибка при распознавании: {e}")

# === Entry point / Точка входа ===
def main():
    global model, DEVICE, FP16

    if torch.cuda.is_available():
        DEVICE = "cuda"
        FP16 = True
        log("⚡ Using GPU (CUDA) / Используем GPU (CUDA)")
    else:
        DEVICE = "cpu"
        FP16 = False
        log("🖥 Using CPU / Используем CPU")

    log(f"CUDA available / CUDA доступна: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        log(f"Device qty: {torch.cuda.device_count()} / Количество устройств: {torch.cuda.device_count()}")
        log(f"Device name: {torch.cuda.get_device_name(0)} / Имя устройства: {torch.cuda.get_device_name(0)}")

    log("🧠 Loading Whisper model / Загружаем модель Whisper...")
    model = whisper.load_model(WHISPER_MODEL, device=DEVICE)

    listen_loop()

if __name__ == "__main__":
    main()
