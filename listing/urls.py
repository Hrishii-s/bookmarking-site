
from django.urls import path,include
from django.views.generic import RedirectView
from listing import views

urlpatterns = [

    path("add_list/",views.addlist,name="addlist"),
    path("view_list/",views.viewlist,name="viewlist"),
    path("signup/",views.signUp,name="signup"),
    path("update/<int:pk>/",views.update,name="updatelist"),
    path("delete/<int:pk>/",views.delete,name="deletelist"),
    path("login/",views.logIn,name="login"),
    path("logout/",views.logOut,name="logout"),
    path("search/",views.search,name="search"),
   
]
