from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.index.as_view(template_name='project_management/index.html'),name='index')
]
