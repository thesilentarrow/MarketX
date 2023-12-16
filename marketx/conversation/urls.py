from django.urls import path
from . import views
app_name='conversation'
urlpatterns=[
    path('', views.inbox, name='inbox'),
    path('<int:item_pk>/',views.new_conversation, name='new'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
