from django.shortcuts import render
from .form import QRcodeForm
import pyqrcode
import png
from pyqrcode import QRCode
import uuid
from pathlib import Path
import os
from django.http import HttpResponse
from django.template import loader
import io
from django.http import FileResponse


def home(request):
    form = QRcodeForm()
    return render(request, 'index.html',{'form':form})




def convert(request):
    uuidFilename=str(uuid.uuid4())
    BASE_DIR = Path(__file__).resolve().parent.parent
    text=request.GET['qrcodeInput']
    print(text)
    form = QRcodeForm()
    url = pyqrcode.create(text)
    qrcodeFilename=os.path.join(BASE_DIR, 'qrcodeimages', uuidFilename+'.png')
    a=url.png(qrcodeFilename, scale=6)
    print(a)

    context={'form':form,'qrcodeFilename':qrcodeFilename}
    template = loader.get_template('index.html')
    img = open(qrcodeFilename, 'rb')
    response = FileResponse(img)
    return response
