from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("read/",views.read,name="read"),
    path("read_one/<str:pk>/",views.readOne,name="read_one"),
    path("create/",views.create,name="create"),
    path("update/<str:pk>/",views.update,name="update"),
    path("delete/<str:pk>/",views.delete,name="delete"),
    path("register/",views.register_user.as_view(),name="register"),
]