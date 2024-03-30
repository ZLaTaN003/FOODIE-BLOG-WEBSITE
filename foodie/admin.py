from django.contrib import admin
from foodie.models import FoodItem,Comment,Review,CategoryList

class FoodItemsAdmin(admin.ModelAdmin):
    exclude = ["food_slug"]

admin.site.register(FoodItem,FoodItemsAdmin)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(CategoryList)