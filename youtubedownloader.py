# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup as bs
import requests
from pytube import YouTube
print("WELCOME TO YOUTUBE\n\n\n\n\n")
print("SELECT THE OPTION YOU WANT TO PERFORM\n1)TRENDINGS\n2)SEARCH\n3)PLAYLISTS")
n=int(input())
# Show the trending page
if n==1:
    
    print("TRENDINGS")
    for i in range(0,100):
        print("*",end=" ")
    res=requests.get("https://www.youtube.com/feed/trending")
    page = res.text
    soup=bs(page,'html.parser')
    vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    videolist=[] # It keeps the record of all the videos
    videolinks=[]  # It keeps record of all the links
    count=0 # It keeps count of videos searched
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
        print("The index of video to download it")
        down=int(input())
        print(videolinks[down])
        yt = YouTube(videolinks[down])
        print("VIDEO YOU ASKED TO DOWNLOAD IS")
        print(yt.title)
        print(yt.streams.all())
        stream=yt.streams.first()
        stream.download()
        
# Search
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
        print("The index of video to download it")
        down=int(input())
        print(videolinks[down])
        yt = YouTube(videolinks[down])
        print("VIDEO YOU ASKED TO DOWNLOAD IS")
        print(yt.title)
        print(yt.streams.all())
        stream=yt.streams.first()
        stream.download()
# My playlists
elif n==3:
    playlist=["https://www.youtube.com/user/MIT/videos","https://www.youtube.com/channel/UChPRO1CB_Hvd0TvKRU62iSQ/videos","https://www.youtube.com/channel/UCXsXitjiT_8qPgNEFGPVfBA/videos","https://www.youtube.com/channel/UCOhHO2ICt0ti9KAh-QHvttQ/videos","https://www.youtube.com/user/GaryVaynerchuk/videos"]
    count=0
    for item in playlist:
        res=requests.get(item)
        page=res.text
        soup=bs(page,'html.parser')
        name=soup.findAll('h1')
        for tag in name:
            title=tag.find('a',attrs={'class':'spf-link'})
            print(str(count)+ " "+title.text)
            count=count+1
    print("select The channel")
    n=int(input())
    res=requests.get(playlist[n])
    page=res.text
    soup=bs(page,'html.parser')
    vids=soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    videolist=[]
    videolinks=[]
    count=0
    for v in vids:
        num=str(count)
        tmp= v['title']
        print(num+"==> "+tmp+"\n\n")
        count=count+1
        videolist.append(tmp)
        links= "https://youtube.com" +v['href']
        videolinks.append(links)
    n=int(input("Want to download anything?"))
    if n==1:
        print("The index of video to download it")
        down=int(input())
        print(videolinks[down])
        yt = YouTube(videolinks[down])
        print("VIDEO YOU ASKED TO DOWNLOAD IS")
        print(yt.title)
        print(yt.streams.all())
        stream=yt.streams.first()
        stream.download()
#     for i in range(0,100):
#         print("*",end=" ")
#     res=requests.get("https://www.youtube.com/user/MIT/videos")
#     page = res.text
#     soup=bs(page,'html.parser')
#     vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
#     name=soup.findAll('h1')
#     for tag in name:
#         title=tag.find('a',attrs={'class':'spf-link'})
#         print(title.text)
#     videolist=[]
#     videolinks=[]
#     count=0
#     for v in vids:
#         num=str(count)
#         tmp =  v['title']
#         print(num+"=>  "+tmp+"\n\n")
#         count=count+1
#         videolist.append(tmp)
#         links= "https://youtube.com" +v['href']
#         videolinks.append(links)
#     n=int(input("WANT TO DOWNLOAD ANYTHING?(1-yes,2-no)"))
#     if n==1:
#         download()
#     print("\n\n\n")
#     print("TECHNICAL GURUJI")
#     for i in range(0,100):
#         print("*",end=" ")
#     res=requests.get("https://www.youtube.com/channel/UCOhHO2ICt0ti9KAh-QHvttQ/videos")
#     page=res.text
#     soup=bs(page,'html.parser')
#     vids=soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
#     for v in vids:
#         num=str(count)
#         tmp=v['title']
#         print(num+"=> "+tmp+"\n\n")
#         count=count+1
#         videolist.append(tmp)
#         links= "https://youtube.com" +v['href']
#         videolinks.append(links)
#     n=int(input("WANT TO DOWNLOAD ANYTHING?(1-yes,2-no)"))
#     if n==1:
#         download()

