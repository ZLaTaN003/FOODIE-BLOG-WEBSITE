from django import forms
from .models import FoodItem,CategoryList


    
class AddFood(forms.ModelForm):
    CHOICES = CategoryList.objects.values_list("name","name") #gets the queryset as [("sweet"),("sweet")] for choice field
    category = forms.ChoiceField(choices=CHOICES,widget=forms.Select)  # havent used Select(attrs={})

    class Meta:
        model = FoodItem
        fields = ["food_name","food_description","food_price","image_url","category"]
        #widgets = can be used here also

class AddComments(forms.Form):
    comment = forms.CharField(max_length=120)