from django.urls import path, include
from . import views

urlpatterns = [

    path('log', views.log, name='log'),
    path('view', views.view, name='view'),
    path('resolve', views.resolve, name='resolve'),
    path('viewstatus', views.viewstatus, name='viewstatus'),
    path('statistic', views.statistic, name='statistic'),
    path('computer_science', views.computerscience, name='computerscience'),
    path('Mechanical_Engginering', views.mechanical, name='mechanical'),
    path('ETC', views.etc, name='etc'),
    path('Civil', views.civil, name='civil'),
    path('Electrical_Enginering', views.electric, name='electric'),
    path('Faculty', views.faculty, name='faculty'),
    path('<int:grievance_id>/approve', views.approve, name='approve'),
    path('<int:grievance_id>/resolvefeedback', views.resolvefeedback, name='resolvefeedback'),
    path('<int:grievance_id>/reject', views.reject, name='reject'),
    path('<int:grievance_id>/status', views.status, name='status'),



    ]
