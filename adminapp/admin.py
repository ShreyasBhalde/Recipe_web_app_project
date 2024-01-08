from django.contrib import admin
from .models import category,recipe

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name']

class recipesAdmin(admin.ModelAdmin):
    list_display = ['id','recipe_name','shortinfo','ingredients','description','steps','image','addedby','cat_fk']


admin.site.register(recipe,recipesAdmin)
admin.site.register(category,categoryAdmin)

