from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')     # 定制显示的字段
    list_filter = ('status', 'created', 'publish', 'author')    # 定制过滤器
    search_fields = ('title', 'body')       # 定制搜索栏
    prepopulated_fields = {'slug':('title',)}   # 根据title自动填充slug字段
    raw_id_fields = ('author',)         # 定制author字段可以用id来填充
    date_hierarchy = 'publish'      # 定制日期导航栏
    ordering = ('status', 'publish')        # 定制排序字段