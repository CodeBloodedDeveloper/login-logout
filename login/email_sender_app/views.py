from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status

from rest_framework import generics
from rest_framework import viewsets

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse 
import traceback
from django.core.mail import send_mail
from django.template import loader


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
         # inject the respective values in HTML template
        html_message = loader.render_to_string(
            'message.html',
            {
                # TODO: Enter the recipient name
                'name': name,
                # TODO:  Update with your own body
                'body': message,
                # TODO: Update the signature
                'sign': name,
            })
        send_mail(
            subject,
            'You are lucky to receive this mail.',
            'vibesdjangologinapp@gmail.com',  # TODO: Update this with your mail id
            ['awasthiharshil12@gmail.com'],  # TODO: Update this with the recipients mail id
            html_message=html_message,
            fail_silently=False,
        )

        return render(request,'success.html')
    