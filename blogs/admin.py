from django.contrib import admin
from .models import Category ,Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tittle',)}
    list_display= ('tittle', 'category', 'status','author', 'is_featured')
    search_fields = ('id', 'tittle', 'category__category_name', 'status')
    list_editable=('is_featured',)



admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)