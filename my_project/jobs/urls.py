from django.urls import path
from jobs import views

urlpatterns = [
    # 127.0.0.1:8000/jobs
    path('', views.show_jobs, name='jobs'),
    path('single/<jid>', views.show_single_job, name='single_job'),
    # path('searched', ''),
    # path('category', '')
]
