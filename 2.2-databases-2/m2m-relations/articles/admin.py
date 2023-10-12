from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


# class ScopeInline(admin.TabularInline):
#     model = Scope
#     extra = 1
#
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [ScopeInline]
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
            if count == 0:
                raise ValidationError('Какая-то ошибка')
            else:
                pass
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    pass
