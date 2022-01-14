from django.contrib import admin

# Register your models here.
from .models import Movie, Artist, MovieArtist, User
# from .forms import UserCreateForm
from django.contrib.auth.admin import UserAdmin

admin.site.register(Movie)
admin.site.register(Artist)
admin.site.register(MovieArtist)
admin.site.register(User)

# class MyUserAdmin(UserAdmin):
#     add_form = UserCreateForm
#     model = User
#     list_display = ['username', 'mobile', 'email']
#     fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mobile', 'email')}),
#     ) #this will allow to change these fields in admin module
