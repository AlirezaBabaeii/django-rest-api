from django.urls import path 
from .views import user_create
urlpatterns =[ 
      path('',user_create,name="user_create")        
]