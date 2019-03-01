from django.contrib import admin
from django.urls import path, include
from grievance import views
from django.conf import settings


admin.site.site_header = 'Synergy Grievance System'
admin.site.site_title = 'Synergy Grievance System'
admin.site.index_title = 'Synergy Grievance System'

urlpatterns = [
    path('synergyadmingrievance/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('grievance/', include('grievance.urls')),

]
