from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('' ,views.hello ,name='hello'),
    path('product_list/', views.product_list, name='product_list'),
    path('clear_cart/' ,views.clear_cart ,name='clear_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product_detail/<int:product_id>/', views.product_detail ,name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('history/', views.history, name='history'),
] 