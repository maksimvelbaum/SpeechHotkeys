# SpeechHotkeys


[[Creator Website ]](https://velbaum.cc) [[Buy me a coffee]](https://buymeacoffee.com/maksim_velbaum)


## Setup
I used Python 3.13.3 
1. Donwload and install   [Python 3.13.2](https://www.python.org/downloads/)
2. Download and install [AutoHotkeys v2](https://www.autohotkey.com/)  ( tested on Version 2.0.19 ) 
3. Download [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) ( tested on version: 2025-05-01-git-707c04fe06  it also attached on git )
4. Extract ffmpeg somewhere , as example to C:\ffmpeg, open Windows Search and find "Edit the system environment variables" > Advanced > Environment Variables > System Variables > Choose Path and click Edit , New and add C:\ffmpeg\bin  Save and close  (Look pictures in folder 98_README_PICTURES )
5. Open PowerShell with Admin Rights and paste "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
 ```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
6.Open PowerShell or CMD and check python version  "python --version" if it is Python 3.13.3 we are good to go 
 ```bash
python --version
```
7. Go back to folder SpeechHotkeys  and start 01_install  (Run anyway)  or make install from terminal (CMD/PowerShell) to see errors "cmd /c 01_install.bat"
   
```bash
cmd /c 01_install.bat
```
I recommend to make install from terminal , in this case you will able to see error if they will appear.

8. 01_install.bat will launch programm BUT most likely it will run on CPU , what is very slow, so close procgramm by clicking Ctrl+C

9 Here you need to decide do you want use GPU for for Whisper AI or you will stay on CPU, if yu will stay on CPU proceed to step ...
 
10.  If you ant you GPU, open terminal in folder and paste in terminal 
    
```bash
.\venv\Scripts\activate
```    
11.  Intall pytorch == torch , I recommend to ask GPT wich version you need to install ,  ONLY FOR EXMAPLE I posting here for my video card RTX 3080

```bash
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cu118
```   
12. When installed , check that it is working
```bash
python -c "import torch; print(torch.cuda.get_device_name(0))"
```
13. If you see something like NVIDIA GeForce RTX 3080  all done correctly.  Please do not post any issue about it , I just don't have time to deal with other video cards. 

14. Now we need to choose [Model Card: Whisper](https://github.com/openai/whisper/blob/main/model-card.md) for English will be enought base or even tiny but if you using another language , small is much better choise

15. Open app.py with Notepead or any other IDE for editing.

16. You need to change
```bash
WHISPER_MODEL = according to your choise, just remember large models will take too much time to proceed , for CPU will be better small models
THRESHOLD  = MIC sensivity ,  less number more sensetive
LANGUAGE = set language code
hotkey0 = "" == if this word will be found in reply from Whisper, key 0 will be send to Autohotkeys
hotkey1 = "" == key 1
hotkey2 = "" == key 2
hotkey3 = ""
hotkey4 = ""
hotkey5 = ""
hotkey6 = ""
hotkey7 = ""
hotkey8 = ""
hotkey9 = ""
stop_word = "стоп"  stop word for stoping script 
stop_word2 = "stop"  stop word for stoping script 
```



