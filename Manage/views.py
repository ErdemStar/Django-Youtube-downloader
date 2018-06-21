# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.template import loader
PY = ""
from pytube import YouTube

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
    if request.method == "GET":
        return render(request, "download.html", {"ad" : PY.title ,"id" : PY.video_id })
    if request.method == "POST":
        tmp = request.POST["type"]
        print tmp
        return render(request, "download.html", {"ad" : "asd" ,"id" : "asd"})




