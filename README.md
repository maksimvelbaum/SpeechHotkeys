[[Creator Website]](https://velbaum.cc) [[Buy me a coffee]](https://buymeacoffee.com/maksim_velbaum)

## Setup

I used Python 3.13.3

1. Download and install [Python 3.13.2](https://www.python.org/downloads/)
2. Download and install [AutoHotkey v2](https://www.autohotkey.com/) (tested on version 2.0.19)
3. Download [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) (tested on version: 2025-05-01-git-707c04fe06 — also attached in the repo)
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



