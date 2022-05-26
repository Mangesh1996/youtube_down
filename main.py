"""
Download the youtube video multiple resoluation 
find_resoluation.py and main.py
usage :- python3 main.py -l youtube_link -p dowload_path

"""
#import the libaray
from ast import arguments
from genericpath import exists
from pytube import YouTube
from time import sleep
from random import randint
import os
import argparse

def resoulation_find(url):
    yt=YouTube(url)
    filters=yt.streams.filter(only_video=True,file_extension="mp4",adaptive=True).order_by("resolution")
    st={i.resolution for i in filters }
    st=" ".join(st).split("p")[:-1]
    lsts=[int(i) for i in st ]
    lsts.sort()
    resoul=[ f"{i}p" for i in lsts]
    return resoul
def save_path(download_path):
    try:
        if os.path.exists(download_path):
            print("download directory are present")
        else:
            os.mkdir(download_path)
            print("Direcotry create done")
    except OSError:
        print(f"directory not created {download_path}")
def youtube_download(download_path,links):
    link=links
    # download_path=input(f"Paster the download path:-   ")
    if download_path =="Default" or download_path=="save":
        save_path(download_path)
    else:
        download_path
    path=os.path.join(os.getcwd(),download_path)
    # get the input link
    
    #make the try to handle error
    try:
        yt=YouTube(link)
        print(yt.title)
    #make the excepthe when the connection issue
    except:
        print("connection error")
    # call the function for check resoluation
    pixl=resoulation_find(link)
    print("Select Video resoluation :- ")
    for i in range(len(pixl)):
        print(f"{i+1}."+pixl[i])
    choice=int(input("Choice the resoulation  :- "))

    mp4files=yt.streams.filter(res=pixl[choice-1]).first()
    try:
        # download the video to save path with vide title name
        mp4files.download(path,filename=f"{yt.title}_{pixl[choice-1]}.mp4")
    except:
        print("some error")

    print(f"downloading complete {yt.title}.mp4")

    sleep(randint(5,10))

def args_parse():
    parser=argparse.ArgumentParser()
    parser.add_argument("-l","--link",help="paste the youtube link",required=True)
    parser.add_argument("-p","--path",help="set download path",required=True)
    argument=parser.parse_args()
    link=argument.link
    path=argument.path
    youtube_download(path,link)


if __name__ =="__main__":
    args_parse()

