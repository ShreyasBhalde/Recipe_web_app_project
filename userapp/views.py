from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse
from adminapp.models import category,recipe
from userapp.models import profile
from django.utils.dateparse import parse_date

def Homepage(request):
    cats=category.objects.all()
    recipes=recipe.objects.all()
    return render(request,"Homepage.html",{"cats":cats,"recs":recipes})

def showrecipes(request, id=None):
    cats = category.objects.all()
    if id:
        cat = get_object_or_404(category, id=id)
        recs = recipe.objects.filter(cat_fk=cat)
    else:
        cat = None
        recs = recipe.objects.all()
    return render(request, "Homepage.html", {"recs": recs, "cats": cats, "cat": cat})

def viewdetails(request,id):
    recipes= recipe.objects.get(id=id)
    cats= category.objects.all()
    return render(request,"viewdetails.html",{"recipe":recipes,"cats":cats})

def signup(request):
    if(request.method =="GET"):
        return render(request,"signup.html",{})
    else:
        username=request.POST["uname"]
        password=request.POST["pwd"]
        email=request.POST["email"]
        number=request.POST["phone"]
        try :
            user=profile.objects.get(username=username)
        except :
            user=profile(username,password,email,number)
            user.save()
            return redirect(Homepage)
        else:
            return redirect(signup)
        
def login(request):
    if(request.method =="GET"):
        return render(request,"login.html",{})
    else:
        username=request.POST["uname"]
        password=request.POST["pwd"]
        try :
            user=profile.objects.get(username=username,password=password)
        except :
            return redirect(login)
        else:
            request.session["uname"]=username
            return redirect(Homepage)

def logout(request):
    request.session.clear()
    return redirect(Homepage)

def account(request):
    details = profile.objects.get(username=request.session.get("uname"))
    uname = request.session.get("uname")
    recipes = recipe.objects.filter(addedby=uname)
    return render(request,"account.html",{"detail" : details,"recipes":recipes})


def addrecipe(request):
    if request.method == "POST":
        recipe_name = request.POST['recipe_name']
        shortinfo = request.POST['shortinfo']
        ingredients = request.POST['ingredients']
        description = request.POST['description']
        steps = request.POST['steps']
        uploading_date = parse_date(request.POST['uploading_date'])
        image = request.FILES['image']
        addedby = request.POST['addedby']
        category_name = request.POST['category']

        try:
            # Fetch the selected category instance
            category_instance = category.objects.get(cat_name=category_name)
        except category.DoesNotExist:
            # If the category doesn't exist, create a new one
            category_instance = category.objects.create(cat_name=category_name)

        try:
            # Check if the recipe already exists
            existing_recipe = recipe.objects.get(recipe_name=recipe_name)
            return redirect(addrecipe)
        except recipe.DoesNotExist:
            # If the recipe doesn't exist, create a new one
            new_recipe = recipe(
                recipe_name=recipe_name,
                shortinfo=shortinfo,
                ingredients=ingredients,
                description=description,
                steps=steps,
                uploading_date=uploading_date,
                image=image,
                addedby=addedby,
                cat_fk=category_instance  # Assign the category instance
            )
            new_recipe.save()
            return redirect(account)
    return render(request, "addrecipe.html", {})
            

def editrecipe(request, recipe_id):
    existing_recipe = get_object_or_404(recipe, id=recipe_id)
    categorie = category.objects.all()
    print(categorie)

    if request.method == "POST":
        # Update the existing recipe with the new values
        existing_recipe.recipe_name = request.POST['recipe_name']
        existing_recipe.shortinfo = request.POST['shortinfo']
        existing_recipe.ingredients = request.POST['ingredients']
        existing_recipe.description = request.POST['description']
        existing_recipe.steps = request.POST['steps']
        existing_recipe.image = request.FILES['image']
        existing_recipe.addedby = request.POST['addedby']
        existing_recipe.cat_fk = category.objects.get(id=request.POST['cat_fk']) 

        # Save the updated recipe
        existing_recipe.save()

        return redirect('account')

    return render(request, "editrecipe.html", {'recipe': existing_recipe,'categories': categorie})

def searchrecipes(request):
    query = request.GET.get('query', '')
    recipes = recipe.objects.filter(recipe_name__icontains=query) | recipe.objects.filter(ingredients__icontains=query)
    return render(request, 'searchrecipes.html', {'recipes': recipes, 'query': query})

def aboutus(request):
    return render(request,"about.html")