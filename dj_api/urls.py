from django.urls import path
from .import apis
urlpatterns = [
    path('bookabi/get/',apis.Book_Class_Api.as_view(),name='Book_Class_Api'),
    path('Bookmixins_list/postget/',apis.Bookmixins_list.as_view(),name='Bookmixins_list'),
    path('Bookmixins_up_des/up_des/<int:pk>',apis.Bookmixins_up_des.as_view(),name='Bookmixins_up_des'),
]
