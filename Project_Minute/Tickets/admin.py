from django.contrib import admin
from Tickets.models import  State_Master, User_Master,Task_Master

# Register your models here.
class State_MasterAdmin(admin.ModelAdmin):
    list_display=("state_name","state_code")

admin.site.register(State_Master,State_MasterAdmin)  

class Umser_MasterAdmin(admin.ModelAdmin)



    
# admin.site.register(User_Master)
# admin.site.register(Task_Master)   
