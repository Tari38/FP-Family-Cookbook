from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# specify course choices

COURSE_CHOICES = (
    ("Unspecified", "Unspecified"),
    ("Breakfast", "Breakfast"),
    ("Brunch", "Brunch"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
    ("Starter/Appetizer", "Starter/Appetizer"),
    ("Snack", "Snack"),
    ("Dessert", "Dessert"),
    ("Sweet", "Sweet"),
    ("Afternoon Tea", "Afternoon Tea")
)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    course = models.CharField(max_length = 30, choices = COURSE_CHOICES, default = "Unspecified")
    description = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse("recipes-detail", kwargs={"pk": self.pk})
  
    def __str__(self):
        return self.title