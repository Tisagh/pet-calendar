from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import PasswordResetForm

# call auth user model
User = get_user_model()

# models
class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm
  list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_admin')
  list_filter = ('is_admin',)
  search_fields = ('email', 'first_name', 'last_name',)
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Profile', {'fields': ('first_name', 'last_name')}),
    ('Access', {'fields': ('is_active', 'is_staff', 'is_admin')}),
  )
  add_fieldsets = (
      ('Required Fields', {
          'description': ("User must have an email, first name, and last name."),
            'classes': ('wide',),
          'fields': ('email', 'first_name', 'last_name'),
          }),
      ('Access', {
          'description': ("Access level for this user."),
            'classes': ('wide',),
          'fields': ('is_active', 'is_staff', 'is_admin'),
          }),
      ('Password', {
          'description': ("Optionally enter a password for the user"),
            'classes': ('collapse', 'collapse-closed'),
          'fields': ('password1', 'password2')
          })
      )
  ordering = ('email',)
  filter_horizontal = ()


# register models
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
