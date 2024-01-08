from django.db import models

# Create your models here.
class category(models.Model):
    cat_name = models.CharField(max_length=30)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.cat_name
    

class recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    shortinfo = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.CharField(max_length=200)
    steps = models.TextField()
    image = models.ImageField(default= 'abc.jpg',upload_to = 'Images')
    addedby = models.CharField(max_length=50,default = "admin")
    cat_fk = models.ForeignKey('category',on_delete=models.CASCADE)

    class Meta:
        db_table = "recipe"




