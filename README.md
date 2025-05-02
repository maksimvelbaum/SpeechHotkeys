[[Creator Website]](https://velbaum.cc) [[Buy me a coffee]](https://buymeacoffee.com/maksim_velbaum)

## Setup

**This Setup is useful only if Microsoft’s speech recognizer doesn’t support your native language, this setup provides a great alternative. It lets you use commands in your preferred language without relying on English, if SP supports your native language,  VoiceAttack looks like better choise**

[Supported languages](https://platform.openai.com/docs/guides/speech-to-text/prompting#supported-languages)

This script is using locally [Whisper AI](https://github.com/openai/whisper)

I used Python 3.13.3

1. Download and install [Python 3.13.3](https://www.python.org/downloads/)
2. Download and install [AutoHotkey v2](https://www.autohotkey.com/) (tested on version 2.0.19)
3. Download [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) (tested on version: 2025-05-01-git-707c04fe06)
4. Extract ffmpeg somewhere, for example to `C:\ffmpeg`.  
   Open Windows Search and find "Edit the system environment variables" > Advanced > Environment Variables > System Variables > choose `Path` and click **Edit**, then **New**, and add `C:\ffmpeg\bin`.  
   Save and close.

![1](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/1.png?raw=true)  
![2](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/2.png?raw=true)  
![3](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/3.png?raw=true)  
![4](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/4.png?raw=true)  

6. Open PowerShell with admin rights and paste the following:

![power_shell](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/power_shell.png?raw=true)

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

6. Open PowerShell or CMD and check the Python version with:

```bash
python --version
```

If it shows Python 3.13.3, you're good to go.

7. Go back to the `SpeechHotkeys` folder and run `01_install` (choose "Run anyway"), or run it from terminal (CMD/PowerShell) to see any errors:

```bash
cmd /c 01_install.bat
```

> I recommend running from terminal so you can see errors if they appear.

8. `01_install.bat` will launch the program BUT it will most likely run on the CPU, which is very slow. Close the program with Ctrl+C.

9. Now you need to decide whether you want to use a GPU for Whisper AI or stay on CPU.  
   If you're using CPU, skip to the next step.  
   If you want to use GPU, continue:

10. Open terminal in the project folder and activate the virtual environment:

```bash
.\venv\Scripts\activate
```

11. Install PyTorch. I recommend asking GPT which version to install.  
    ONLY AS EXAMPLE — for my GPU (RTX 3080), I used:

```bash
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

12. After installation, check that CUDA is working:

```bash
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

13. If you see something like `NVIDIA GeForce RTX 3080`, everything is correct.  
    Please don't post issues related to other GPUs — I just don't have time to debug them.

14. Now, choose a [Whisper Model](https://github.com/openai/whisper/blob/main/model-card.md).  
    For English, `base` or even `tiny` is enough.  
    For other languages, `small` is a better choice.  
    Models are stored in:

```bash
C:\Users\_user_\.cache\whisper
```

15. Open `app.py` with Notepad or your IDE of choice.

16. Edit the following settings:

```bash
WHISPER_MODEL =  # choose the model; large ones are slow, use small for CPU
THRESHOLD =  # mic sensitivity; lower number = more sensitive
LANGUAGE =  # set language code
hotkey0 = ""  # if this word is found, key 0 will be sent
hotkey1 = ""
hotkey2 = ""
hotkey3 = ""
hotkey4 = ""
hotkey5 = ""
hotkey6 = ""
hotkey7 = ""
hotkey8 = ""
hotkey9 = ""
stop_word = "стоп"  # stop word to stop the script
stop_word2 = "stop"  # alternative stop word
```

17. The final step is configuring the Autohotkey script.  
    A sample profile for **The Elder Scrolls IV: Oblivion Remastered** is included.  
    (In-game, bind spells to NUM1–NUM9)

![6](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/6.png?raw=true)

Hope it was helpful

[![coffee](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/coffee.gif?raw=true)](https://www.buymeacoffee.com/maksim_velbaum)


[[Сайт разработчика]](https://velbaum.cc) [[Угостить кофе]](https://buymeacoffee.com/maksim_velbaum)

## Установка

**Данная настройка полезна только если распознаватель речи Microsoft не поддерживает ваш родной язык, эта настройка предоставляет отличную альтернативу. Она позволяет использовать команды на вашем предпочитаемом языке без необходимости полагаться на английский. Если SP поддерживает ваш родной язык, VoiceAttack выглядит лучшим выбором**


[Поддерживаемые языки](https://platform.openai.com/docs/guides/speech-to-text/prompting#supported-languages)

Этот скрипт использует локально  [Whisper AI](https://github.com/openai/whisper)

Я использовал Python 3.13.3

1. Скачайте и установите [Python 3.13.2](https://www.python.org/downloads/)
2. Скачайте и установите [AutoHotkey v2](https://www.autohotkey.com/) (проверено на версии 2.0.19)
3. Скачайте [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) (проверено на версии: 2025-05-01-git-707c04fe06)
4. Распакуйте ffmpeg куда-нибудь, например в `C:\ffmpeg`.  
   Откройте поиск Windows и найдите "Изменить системные переменные среды" > Дополнительно > Переменные среды > Системные переменные > выберите `Path` и нажмите **Изменить**, затем **Создать**, и добавьте `C:\ffmpeg\bin`.  
   Сохраните и закройте.

![1](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/1.png?raw=true)  
![2](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/2.png?raw=true)  
![3](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/3.png?raw=true)  
![4](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/4.png?raw=true)  

6. Откройте PowerShell с правами администратора и вставьте следующее:

![power_shell](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/power_shell.png?raw=true)

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

6. Откройте PowerShell или CMD и проверьте версию Python с помощью:

```bash
python --version
```

Если отображается Python 3.13.3, всё в порядке.

7. Вернитесь в папку `SpeechHotkeys` и запустите `01_install` (выберите "Выполнить в любом случае"), или запустите его из терминала (CMD/PowerShell), чтобы увидеть ошибки, если они есть:

```bash
cmd /c 01_install.bat
```

> Рекомендую запускать из терминала, чтобы видеть ошибки, если они появятся.

8. `01_install.bat` запустит программу, НО, скорее всего, она будет работать на CPU, что очень медленно. Закройте программу с помощью Ctrl+C.

9. Теперь вам нужно решить, хотите ли вы использовать GPU для Whisper AI или оставить CPU.  
   Если вы используете CPU, переходите к следующему шагу.  
   Если вы хотите использовать GPU, продолжайте:

10. Откройте терминал в папке проекта и активируйте виртуальное окружение:

```bash
.\venv\Scripts\activate
```

11. Установите PyTorch. Я рекомендую спросить у GPT, какую версию установить.  
    ТОЛЬКО В КАЧЕСТВЕ ПРИМЕРА — для моего GPU (RTX 3080) я использовал:

```bash
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

12. После установки проверьте, что CUDA работает:

```bash
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

13. Если вы видите что-то вроде `NVIDIA GeForce RTX 3080`, всё правильно.  
    Пожалуйста, не публикуйте проблемы, связанные с другими GPU — у меня просто нет времени их отлаживать.

14. Теперь выберите [Модель Whisper](https://github.com/openai/whisper/blob/main/model-card.md).  
    Для английского языка достаточно `base` или даже `tiny`.  
    Для других языков лучше выбрать `small`.  
    Модели хранятся в:

```bash
C:\Users\_пользователь_\.cache\whisper
```

15. Откройте `app.py` с помощью Блокнота или вашей IDE.

16. Отредактируйте следующие настройки:

```bash
WHISPER_MODEL =  # выберите модель; большие медленные, используйте small для CPU
THRESHOLD =  # чувствительность микрофона; меньшее число = более чувствительный
LANGUAGE =  # установите код языка
hotkey0 = ""  # если это слово найдено, будет отправлена клавиша 0
hotkey1 = ""
hotkey2 = ""
hotkey3 = ""
hotkey4 = ""
hotkey5 = ""
hotkey6 = ""
hotkey7 = ""
hotkey8 = ""
hotkey9 = ""
stop_word = "стоп"  # стоп-слово для остановки скрипта
stop_word2 = "stop"  # альтернативное стоп-слово
```

17. Последний шаг — настройка скрипта Autohotkey.  
    Пример профиля для **The Elder Scrolls IV: Oblivion Remastered** включен.  
    (В игре привяжите заклинания к NUM1–NUM9)

![6](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/6.png?raw=true)

Надеюсь, это было полезно

[![coffee](https://github.com/maksimvelbaum/SpeechHotkeys/blob/main/98_README_PICTURES/coffee.gif?raw=true)](https://www.buymeacoffee.com/maksim_velbaum)



