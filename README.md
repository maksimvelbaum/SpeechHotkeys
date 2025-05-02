# SpeechHotkeys


[[Creator Website ]](https://velbaum.cc)


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
