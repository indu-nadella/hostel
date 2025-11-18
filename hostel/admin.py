from django.contrib import admin
from hostel.models import HostelPersonDetails,HostelFeeDetails,HostelMenu

# Register your models here.
admin.site.register(HostelPersonDetails)
admin.site.register(HostelFeeDetails)
admin.site.register(HostelMenu)