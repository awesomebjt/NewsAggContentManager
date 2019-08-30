from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("nacman index")

def post(request, post_id):
    response = "You are looking at post %s"
    return HttpResponse(response % post_id)


