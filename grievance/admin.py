from django.contrib import admin

from . models import Grievance

class PostAdmin(admin.ModelAdmin):
    list_display =["Name","title","re_date","v_date","r_date"]
    list_display_links=["r_date","re_date","v_date"]
    list_filter = ["r_date","v_date","re_date"]
    list_per_page = 25

    class Meta:
        model = Grievance

admin.site.register(Grievance, PostAdmin)
