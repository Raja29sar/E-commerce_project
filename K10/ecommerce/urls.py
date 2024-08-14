from django.urls import path
from ecommerce import views


urlpatterns = [
   path('',views.ecommerce,name="ecommerce"),
   path('insert',views.insertData,name="insertData"),
]