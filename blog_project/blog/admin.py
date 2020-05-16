from django.contrib import admin
from .models import Article,Category,TitleSettings

# Register your models here.


# ساخت اکشن برای پنل ادمین برای منتشر ساختن مقاله ها
def make_published(self, request, queryset):
    rows_updated = queryset.update(status = 'p')
    if rows_updated == 1:
        message_bit = "یک مقاله به حالت انتشار در آمد"
    else:
        message_bit = "%s مقاله به حالت انتشار در آمد" % rows_updated
    self.message_user(request, message_bit)
make_published.short_description = "انتشار مقاله های انتخاب شده"


# ساخت اکشن برای پنل ادمین برای پیش نویس کردن مقاله ها
def make_draft(self, request, queryset):
    rows_updated = queryset.update(status = 'd')
    if rows_updated == 1:
        message_bit = "یک مقاله به حالت پیش نویس در آمد"
    else:
        message_bit = "%s مقاله به حالت پیش نویس در آمد" % rows_updated
    self.message_user(request, message_bit)
make_draft.short_description = "عدم انتشار مقاله های انتخاب شده"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title','parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status', '-publish']
    actions = [make_published,make_draft]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = "دسته بندی"

admin.site.register(Article, ArticleAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('position', 'title',)
    search_fields = ('title', 'position')

admin.site.register(TitleSettings, SettingsAdmin)