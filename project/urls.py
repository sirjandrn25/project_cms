from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="home"),
    path("categories/",CategoryView.as_view(),name="category"),
    path("delete_category/<int:id>/",delete_category,name="delete_category"),
    path("update_category/<int:id>/",update_category,name="update_category"),
    path("project/",ProjectView.as_view(),name="project"),
    path("add_project/",AddProjectView.as_view(),name="add_project"),
]
