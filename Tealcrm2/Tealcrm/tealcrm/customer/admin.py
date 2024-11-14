from django.contrib import admin

from .models import CustomerUserProfile, Customer_details, task, SupportTicket

admin.site.register(CustomerUserProfile)
admin.site.register(Customer_details)
admin.site.register(task)
admin.site.register(SupportTicket)

