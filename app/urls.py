from django.urls import path
from .import views
urlpatterns=[
path('',views.signup,name='signup'),
path('/home',views.base,name='base'),
path('/booking',views.booking,name='booking'),
path('/detail',views.detail,name='detail'),
path('/logout',views.logout,name='logout'),
path('update/<int:pk>',views.update,name='update'),
path('delete/<int:pk>',views.delete,name='delete'),
]

