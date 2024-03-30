from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import FoodItem,Comment,Review,CategoryList
from .forms import AddFood,AddComments
from django.db.models import Count
# Create your views here.


def food_list(request):
    """
    List view for all the food items
    """
    all_food_items = FoodItem.objects.all().order_by("-date_published")
    ctx = {"all_food":all_food_items}
    return render(request,"foodie/food.html",context=ctx)

    

def food_detail(request,slug_food): #addcomment here
    """
    This view displays the detailed page and also comment processing logic is here also the reviews which is most in number
    """
    food = FoodItem.objects.get(food_slug=slug_food)
    most_selected = Review.objects.filter(fooditem=food).values('rating').annotate(count=Count('rating')).order_by('-count').first()
    trending = None
    if most_selected:
          rating_key = most_selected["rating"]
          trending = Review.review[rating_key]
    
    form = AddComments()
    comments = food.comment_set.all()
    if request.method == "POST":
        form = AddComments(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            comment_to_post = Comment.objects.create(fooditem=food,comment=comment)
            comment_to_post.save()

            redirect(request.path_info)
    
    ctx = {"food":food,"form":form,"comments":comments,"trending":trending}
    return render(request,"foodie/food_detail.html",context=ctx)


def add_food(request):
    """
    This view is responsible to Create Food Models
    """
    form = AddFood()
    if request.method == "POST":
        form = AddFood(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("food_list"))
    ctx = {"form":form}
    return render(request,"foodie/add_food.html",context=ctx)


def add_review(request,slug_food):
    """
    This view is refrenced by the form action which helps me put 2 forms in one template
    """
    fooditem = FoodItem.objects.get(food_slug=slug_food)
    if request.method == "POST":
        rating_to_save = request.POST["review"]
        Review.objects.create(fooditem=fooditem,rating=rating_to_save) #saves for ex- A to rating (key of review dict)
        return redirect(reverse('food_detail', kwargs={'slug_food': slug_food}))


def edit_food(request,slug_food):
    food_to_edit = FoodItem.objects.get(food_slug=slug_food)
    if request.method == "POST":
        form = AddFood(request.POST,instance=food_to_edit)
        if form.is_valid():
             form.save()
             return redirect(reverse("food_list"))
    else:
        form = AddFood(instance=food_to_edit)

    ctx = {"form":form}
    return render(request,"foodie/add_food.html",context=ctx)


def delete_food(request,slug_food):
    food_to_delete = FoodItem.objects.get(food_slug=slug_food)
    food_to_delete.delete()
    return  redirect(reverse("food_list"))


def delete_comment(request,slug_food,comment_id):
    if request.method == "POST":
       food = FoodItem.objects.get(food_slug=slug_food)
       comment_to_delete = Comment.objects.get(id=comment_id, fooditem=food)
       comment_to_delete.delete()
       return  redirect(reverse("food_detail",kwargs={'slug_food':slug_food}))
    
def most_reviewed(request):
    best_foods = FoodItem.objects.filter(review__rating = "A")
    ctx = {"best_food":best_foods}

    return render(request,"foodie/bestfoods.html",context=ctx)


def category(request):

    #all_foods = FoodItem.objects.all()   // wont work as when i loop it in template cant get distinct categories  values get repeated
    items_to_display = FoodItem.objects.filter(active=True)
    category = None
    error = None

    categories = FoodItem.objects.values_list('category', flat=True).distinct()
    print(categories)


    if request.method == "POST":
        try:
            category = request.POST["chosen"]
        except KeyError:
            error = "Please select a value"
        if category:
            items_to_display = FoodItem.objects.filter(active=True,category=category)
        print(category)
    ctx = {"categories":categories,"items_to_display":items_to_display,"error": error}

    return render(request,"foodie/category.html",context=ctx)

  