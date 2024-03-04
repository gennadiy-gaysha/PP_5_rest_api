from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_at', 'email_display', 'image')
    def email_display(self, obj):
        return obj.email
    email_display.short_description = 'Email'

admin.site.register(Profile, ProfileAdmin)


