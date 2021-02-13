# youtube-channel-audio-downloader


# Dependency 

# 셀레늄 및  게코드라이버 그리고 FFMPEG, parallel, youtube-dl

pip install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz

tar -xf geckodriver-v0.29.0-linux64.tar.gz

sudo mv geckodriver  /usr/local/bin/

sudo snap install ffmpeg

sudo apt install parallel

sudo wget https://yt-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl

sudo chmod a+x /usr/local/bin/youtube-dl

hash -r

youtube-dl -U


# MAIN INSTALL 

터미널 창에서 입력 

git clone https://github.com/seominlee/youtube-channel-audio-downloader

다운로드 폴더로 가서 

mkdir mp3

mkdir m4a



# TEST !!!

time python3 mp3.py https://www.youtube.com/user/jervilan/featured

time python3 m4a.py https://www.youtube.com/user/jervilan/featured


작업을 마치면  각각  MP3 폴더 및  M4A 폴더에 저장됨.

