from pytube import YouTube

yt = YouTube('https://youtu.be/a3ICNMQW7Ok?si=0jZSGTsaR-pWPwcX')

video = yt.streams.get_by_itag(18)

video.download()