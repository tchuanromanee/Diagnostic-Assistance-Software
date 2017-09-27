from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from diagassist.models import Therapist, Client, Diagnostic

# Define an inline admin descriptor for Therapist model
# which acts a bit like a singleton
class ClientInline(admin.TabularInline):
	model = Client
	
class TherapistInline(admin.TabularInline):
	model = Therapist
	inlines = [ClientInline]

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [TherapistInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class DiagnosticAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'page']}),
		('Coding Information', {'fields': ['ICD9', 'ICD10'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'ICD9', 'ICD10')
	search_fields = ['name']
	

admin.site.register(Diagnostic, DiagnosticAdmin)