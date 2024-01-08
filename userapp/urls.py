from django.urls import path
from . import views 

urlpatterns =[
    path('',views.Homepage),
    path('showrecipes/<id>',views.showrecipes),
    path('viewdetails/<id>',views.viewdetails),
    path('signup',views.signup),
    path('login',views.login),
    path('account',views.account),
    path('logout',views.logout),
    path('addrecipe',views.addrecipe),
    path('editrecipe/<recipe_id>',views.editrecipe),
    path('searchrecipes/',views.searchrecipes),
    path('aboutus/',views.aboutus),

]