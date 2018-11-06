# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup as bs
import requests
from pytube import YouTube
print("WELCOME TO YOUTUBE\n\n\n\n\n")
print("SELECT THE OPTION YOU WANT TO PERFORM\n1)TRENDINGS\n2)SEARCH\n3)PLAYLISTS")
n=int(input())
if n==1:
    
    print("TRENDINGS")
    for i in range(0,100):
        print("*",end=" ")
    res=requests.get("https://www.youtube.com/feed/trending")
    page = res.text
    soup=bs(page,'html.parser')
    vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    videolist=[]
    videolinks=[]
    count=0
    for v in vids:
        num=str(count)
        tmp =  v['title']
        print(num+"=>  "+tmp+"\n\n")
        count=count+1
        videolist.append(tmp)
        links= "https://youtube.com" +v['href']
        videolinks.append(links)
    n=int(input("WANT TO DOWNLOAD ANYTHING?(1-yes,2-no)"))
    if n==1:
        download()
elif n==2:
    search=input("ENTER YOUR QUERY")
    for i in range(0,100):
        print("*",end=" ")
    query="https://www.youtube.com/results?search_query="+search
    res2=requests.get(query)
    page=res2.text
    soup2=bs(page,'html.parser')
    vids2=soup2.findAll('a',attrs={'class':'yt-uix-tile-link'})
    searchvideos=[]
    videolinks=[]
    count=0
    for v in vids2:
        num=str(count)
        tmp=v['title']
        print(num+" "+tmp+"=> ")
        count=count+1
        searchvideos.append(tmp)        
        links= "https://youtube.com" +v['href']
        videolinks.append(links)
    n=int(input("ANYTHING YOU WANT TO DOWNLOAD?"))
    if n==1:
        download()
        
elif n==3:
    print("CARRY MINATI")
    for i in range(0,100):
        print("*",end=" ")
    res=requests.get("https://www.youtube.com/user/AddictedA1/videos")
    page = res.text
    soup=bs(page,'html.parser')
    vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    videolist=[]
    videolinks=[]
    count=0
    for v in vids:
        num=str(count)
        tmp =  v['title']
        print(num+"=>  "+tmp+"\n\n")
        count=count+1
        videolist.append(tmp)
        links= "https://youtube.com" +v['href']
        videolinks.append(links)
    n=int(input("WANT TO DOWNLOAD ANYTHING?(1-yes,2-no)"))
    if n==1:
        download()
    print("\n\n\n")
    print("TECHNICAL GURUJI")
    for i in range(0,100):
        print("*",end=" ")
    res=requests.get("https://www.youtube.com/channel/UCOhHO2ICt0ti9KAh-QHvttQ/videos")
    page=res.text
    soup=bs(page,'html.parser')
    vids=soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    for v in vids:
        num=str(count)
        tmp=v['title']
        print(num+"=> "+tmp+"\n\n")
        count=count+1
        videolist.append(tmp)
        links= "https://youtube.com" +v['href']
        videolinks.append(links)
    n=int(input("WANT TO DOWNLOAD ANYTHING?(1-yes,2-no)"))
    if n==1:
        download()
def download():
        print("The index of video to download it")
        down=int(input())
        yt = YouTube(videolinks[down])
        print("VIDEO YOU ASKED TO DOWNLOAD IS")
        print(yt.title)
        print(yt.streams.all())
        stream=yt.streams.first()
        stream.download()
