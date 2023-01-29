from django.shortcuts import render
from .models import UploadFile, ContentFile
from django.http import HttpResponse


def uploadFileForm(request):
    if request.method == "GET":
      return render(request, "form.html")
    elif request.method == "POST":
        upload_file = request.FILES["file"]
        uploaded_file = UploadFile(file= upload_file, )
        uploaded_file.file.save("CNAB.txt", request.FILES["file"])
        contentFile()
        
        return HttpResponse("Arquivo enviado com sucesso")

def contentFile():
        openFile = open("CNAB.txt", "r")
        readFile = openFile.readlines()
        file= [tuple(a.split(',')) for a in readFile]
        i=0

        while i < len(file):
          for tupla in file:
            type = tupla[i][0]
            date = tupla[i][1:8]
            value = tupla[i][9:18]
            cpf = tupla[i][19:29]
            card = tupla[i][30:41]
            hour = tupla[i][42:47]
            owner = tupla[i][48:61]
            name = tupla[i][62:80]
            content= ContentFile(type=type, date=date, value= int(value), 
            cpf=cpf,card=card,hour=hour,owner=owner,name=name)
            content.save()
          i += 1
          if i == 1:
            i=0
            break