from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class CategoryList(models.Model):
    name = models.CharField(max_length=200)  #model for making choices for modelform of fooditem

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    food_name = models.CharField(max_length=200)
    food_description = models.TextField(max_length=2000)
    food_price = models.IntegerField()
    date_published = models.DateTimeField(null=True,auto_now_add=True)
    image_url = models.CharField(max_length=2000,default="nothing")
    food_slug = models.SlugField(null=False)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=200,null=True)  #even though its a normal char field i make it as select while making a form (modelform widgets)

    def get_absolute_url(self):
        return reverse("food_detail", kwargs={"slug_food": self.food_slug})

    def save(self,*args,**kwargs):
        self.food_slug = slugify(self.food_name)

        super().save(*args,**kwargs)

    def __str__(self):
        return self.food_name


class Comment(models.Model):
    fooditem = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    comment = models.CharField(max_length=80)

    
    def __str__(self):
        return f"{self.comment} on {self.fooditem}"

class Review(models.Model):
    review = {                 # i have tried to add choice to model itself whereas the select for category field in fooditem model is made with django modelform
                               # here on client i used plain html select with hardcoded values  represents the keys of the review dict
        "A":"Delicious",
        "B":"Tasty",
        "C":"Not Bad",           
        "D": "Worst",
    }
    fooditem = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    rating = models.CharField(max_length=1,choices=review)
    
    def __str__(self):
        return f"{self.get_rating_display()} on {self.fooditem}"