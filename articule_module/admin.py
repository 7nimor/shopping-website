from django.contrib import admin
from . import models


# Register your models here.
class AricleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        return super().save_model(request, obj, form, change)


class ArticleComment(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(models.ArticleCategory)
admin.site.register(models.Article, AricleAdmin)
admin.site.register(models.ArticleComment,ArticleComment)
