from multiprocessing.reduction import duplicate
from winreg import QueryInfoKey
from django.shortcuts import render,redirect
from django.views import View
from ..forms import *
from django.contrib import messages
from project.models import *


class ProjectView(View):
    def get(self,request):
        projects = Project.objects.all()
        query = request.GET.get('query')
        status = request.GET.get('status')
        if status:
            if status == 'active':
                projects = Project.objects.filter(is_active=True)
            elif status == "deactive":
                projects = Project.objects.filter(is_active=False)
            
            elif status == "trash":
                projects = Project.objects.filter(trash=True)

        limit = request.GET.get('limit')

        limit = int(limit) if limit else 5
        if query:
            projects = Project.objects.filter(project_name=query)
        context = {
            'projects':list(projects)[:limit],
            'all':len(Project.objects.all()),
            "active":len(Project.objects.filter(is_active=True)),
            'inactive':len(Project.objects.filter(is_active=False)),
            'trash':len(Project.objects.filter(trash=True)),

        }
        return render(request,"projects/index.html",context)
    

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
        ref_links = request.POST.getlist('ref_link')
        
        if form.is_valid():
            project = form.save()
            # save documents 
            for document in documents:
                ProjectDocument.objects.create(document=document,project=project)

            # save reference links 
            for ref_link in ref_links:
                ReferenceLink.objects.create(ref_link=ref_link,project=project)

            messages.info(request,"successfully create new project")
            return redirect("add_project")
        
        
        context = {
            'form':form
        }
        return render(request,"projects/add_project.html",context)

