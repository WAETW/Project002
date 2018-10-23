# Project002
台中教育大學專題
- 專題名稱：實作深度學習影像辨識應用於Raspberry Pi
- 專題組別：NTCU-CS-PRJ-108-10
- 專題成員： 呂晟暐 顏嘉佑 洪聖勛

## 所需套件
- spotipy 需到[Github Repository](https://github.com/plamere/spotipy)更新client.py
- gTTs //用Bing TTS替代
- Speech Recognition
- PyAudio
- Pydub
- Newsapi-python
- googletrans
- requests
- dualogflow
- json
- ffmpeg
- pulseaudio-equalize
### 安裝
```shell
cd Script
sh install_package.sh
```
### ffmpeg
Linux以下列方式進行安裝
To install libav:
``` shell       
~$ apt-get install libav-tools
```
To install ffmpeg:       
```shell
~$ apt-get install ffmpeg
```
### googlestrans
- 因為API進行過改動，所以透過下列指示重新安裝
```shell
~$ pip uninstall googletrans (已安裝過googletrans才需要執行)
~$ git clone https://github.com/BoseCorp/py-googletrans.git
~$ cd ./py-googletrans && python setup.py install
```
### pulseaudio-equalizer
透過安裝pulseaudio-equalizer使wav播放音質正常
```shell
~$ sudo apt-get install pulseaudio-equalizer
```
