from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time', 'id')
    list_filter = ('pub_time', )
    ordering = ('id',)

admin.site.register(Article, ArticleAdmin)
