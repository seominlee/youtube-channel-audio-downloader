#
# youtube-channel-url TO audio files (mp4, flac or m4a)

Download YouTube channel videos to sound source at once

유투브 채널별 비디오들을 한번에 오디오 파일들로 다운로드 (mp3, flac or m4a)


## Dependency install  on Mac OS ( Mac OS 설치 프로그램)

----- firefox, selenium,  geckodriver, FFMPEG, parallel, youtube-dl --------

https://www.mozilla.org/en-US/firefox/new/    (firefox down and install)

```
pip3 install selenium

cd /tmp

wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-macos.tar.gz

tar xf geckodriver-v0.29.0-macos.tar.gz

chmod +x geckodriver

sudo mv geckodriver /usr/local/bin/

brew install ffmpeg

brew install parallel

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl

hash -r

youtube-dl -U
```


## Dependency install on ubuntu 20.04 (우분투 설치 프로그램) 

----- selenium,  geckodriver, FFMPEG, parallel, youtube-dl --------

```
pip install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz

tar -xf geckodriver-v0.29.0-linux64.tar.gz

sudo mv geckodriver  /usr/local/bin/

sudo snap install ffmpeg

sudo apt install parallel

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl

hash -r

youtube-dl -U
```



# MAIN INSTALL (메인 설치)

```
git clone https://github.com/seominlee/youtube-channel-audio-downloader

cd youtube-channel-audio-downloader

mkdir mp3 && mkdir m4a && mkdir flac
```



# TEST !!! 

(python3 mp3.py + youtube channel url)  

(python3 flac.py + youtube channel url) 

(python3 m4a.py + youtube channel url)   


```

time python3 m4a.py https://www.youtube.com/channel/UCoUM-UJ7rirJYP8CQ0EIaHA

time python3 flac.py https://www.youtube.com/channel/UCoUM-UJ7rirJYP8CQ0EIaHA

time python3 mp3.py https://www.youtube.com/user/jervilan/featured

```



saved to mp3, flac or m4a folder.

![alt text](https://github.com/seominlee/youtube-channel-audio-downloader/blob/main/bruno.png)



# videos parsing and saving urls code from : 

https://www.reddit.com/r/DataHoarder/comments/9qrlbp/i_wrote_a_pythonselenium_based_crawler_to_really/
