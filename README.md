# youtube-channel-audio-downloader (mp4 or m4a)


# Dependency install

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


git clone https://github.com/seominlee/youtube-channel-audio-downloader

cd youtube-channel-audio-downloader

mkdir mp3

mkdir m4a



# TEST !!!

time python3 mp3.py https://www.youtube.com/user/jervilan/featured


time python3 m4a.py https://www.youtube.com/user/jervilan/featured


saved to mp3 or m4a folder.


# videos parsing and saving urls code from : 

https://www.reddit.com/r/DataHoarder/comments/9qrlbp/i_wrote_a_pythonselenium_based_crawler_to_really/
