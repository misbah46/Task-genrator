

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),  
    path('logout_view/', views.logoutUser, name="logout"),
    path('dashboard/<str:pk>/', views.dashboard, name = "dash"),
    # path('customer/', views.customer, name = "customers"),
    path('form/', views.form, name = "form" ),



    path('', views.home, name="home"),
    # path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    # path('product/', views.product, name = "products"),

]
#     path('', views.home),
#     path('login/', views.login, name = "login"),
#     path('register/', views.register, name = "registers" ),



# ]