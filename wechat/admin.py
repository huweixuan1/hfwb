from django.contrib import admin

# Register your models here.
from .models import UserInfo,JobInfo,JobTag,HouseTag,House_Trade,Total,Images,CarPool,CarpoolTag,OldCar,EmergencyHelp,LifeService,LookForHelp,OldItem,Comments,Reply

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','openid','sex','province','city','headimgurl',)
    list_filter = ('user',)

admin.site.register(UserInfo,UserInfoAdmin)


class JobInfoAdmin(admin.ModelAdmin):
    list_display = ('user','type','content','contact','tel','img','created')
    list_filter = ('contact',)

admin.site.register(JobInfo,JobInfoAdmin)

class JobTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_filter = ('tag',)

admin.site.register(JobTag,JobTagAdmin)



class HouseTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_filter = ('tag',)

admin.site.register(HouseTag,HouseTagAdmin)


class HouseTradeAdmin(admin.ModelAdmin):
    list_display = ('type','user','detail','position','created')
    list_filter = ('type',)

admin.site.register(House_Trade,HouseTradeAdmin)




admin.site.register(Total)


admin.site.register(Images)
admin.site.register(CarpoolTag)
admin.site.register(CarPool)
admin.site.register(OldCar)
admin.site.register(EmergencyHelp)
admin.site.register(LookForHelp)
admin.site.register(LifeService)
admin.site.register(OldItem)
admin.site.register(Comments)
admin.site.register(Reply)



