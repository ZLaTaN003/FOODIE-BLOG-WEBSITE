from django.urls import path,include
from . import views
urlpatterns = [
    path('foods_listed/',views.food_list,name='food_list'),#viewing list view for food
    path('food_detail/<slug:slug_food>',views.food_detail,name='food_detail'), #viewing detail view comments also in this endpoint
    path('add_fooditem/',views.add_food,name='add_food'),#create for food
    path('food_detail/<slug:slug_food>/reviews',views.add_review,name='review'),#endpoint for review
    path('edit_food/<slug:slug_food>',views.edit_food,name='edit_food'),# edit endpoint for editing food
    path('delete_food/<slug:slug_food>',views.delete_food,name='delete_food'),#delete fooditem
    path('delete_comment/<slug:slug_food>/<int:comment_id>/',views.delete_comment,name='delete_comment'),
    path('best_foods/',views.most_reviewed,name='best_foods'),
    path('category/',views.category,name='category'),


]
