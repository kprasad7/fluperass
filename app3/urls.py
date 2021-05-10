from django.urls import path , include
from . import views


urlpatterns=[
    path('apicreate/', views.Cat_create.as_view(), name='song'),
    path('apiview/', views.Cat_get.as_view(), name='song_put'),
    path('api/<int:pk>/', views.Cat_put.as_view(), name='song_put'),
    
]    