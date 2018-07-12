# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.template import loader
PY = ""
from pytube import YouTube
import os

def Redirect(request):
    return HttpResponseRedirect("index")

def Index(request):
    global PY
    if request.method == "POST":
        url = request.POST["url"]
        PY = YouTube(url)
        return HttpResponseRedirect("/download")
    else:
        return render(request, "index.html", {})

def Download(request):
    global PY
    MusicPath = os.getcwd() + "/Music"

    if request.method == "GET":
        return render(request, "download.html", {"ad" : PY.title ,"id" : PY.video_id })

    if request.method == "POST":
        tmp = request.POST["type"]

        if tmp == "music":
            music = PY.streams.get_by_itag(140)

            if music is None:
                music = PY.streams.filter(subtype='mp4').first()
                music.download(MusicPath)
                print music
            else:
                print music
                music.download(MusicPath)


            return render(request, "download.html", {"ad": PY.title, "id": PY.video_id})

        if tmp == "video":
            videos = PY.streams.get_by_itag(22)

            if videos is None:
                videos = PY.streams.filter(subtype='mp4').filter(progressive=True).first()
                videos.download(MusicPath)
            else:
                videos.download(MusicPath)

            return render(request, "download.html", {"ad": PY.title +"(Video başarıyla indirildi)", "id": PY.video_id})


