from multiprocessing.reduction import duplicate
from django.shortcuts import render,redirect
from django.views import View
from ..forms import *
from django.contrib import messages


class ProjectView(View):
    def get(self,request):

        return render(request,"projects/index.html")
    

class AddProjectView(View):
    def get(self,request):
        form = ProjectAddForm()
        file_form = UploadDocumentForm()

        context = {
            'form':form,
            "file_form":file_form
        }

        return render(request,"projects/add_project.html",context)
    
    def post(self,request):
        form = ProjectAddForm(request.POST)
        documents = request.FILES.getlist('document')
        if form.is_valid():
            project = form.save()
            for document in documents:
                ProjectDocument.objects.create(document=document,project=project)

            messages.info(request,"successfully create new project")
            return redirect("add_project")
        
        
        context = {
            'form':form
        }
        return render(request,"projects/add_project.html",context)

