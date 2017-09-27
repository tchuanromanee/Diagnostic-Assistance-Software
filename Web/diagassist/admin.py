from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from diagassist.models import Therapist

# Define an inline admin descriptor for Therapist model
# which acts a bit like a singleton
class TherapistInline(admin.TabularInline):
    model = Therapist

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [TherapistInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)