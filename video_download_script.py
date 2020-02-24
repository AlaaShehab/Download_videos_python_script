import os

def download():
    urls = open('vid_list', 'r')
    print(urls)
    urls.read()
    urls.close()
    os.system("youtube-dl -o Videos/%(title)s-%(id)s.%(ext)s' -a vid_list --recode-video mp4")

download()