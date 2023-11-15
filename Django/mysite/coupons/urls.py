from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('applica/', views.coupon_applica, name='applica'),
]
