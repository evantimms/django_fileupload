from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
import os

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename, format=None):
        file = request.data['file']

        fn = os.path.abspath(os.path.join(settings.BASE_DIR, 'uploads', file.name))

        destination = open(fn, '+wb')

        for chunk in file.chunks():
            destination.write(chunk)
            print("Written to {}".format(fn))
        return HttpResponse(status=204)