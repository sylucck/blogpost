from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import *
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on','created_on')
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact)
admin.site.register(Profile)