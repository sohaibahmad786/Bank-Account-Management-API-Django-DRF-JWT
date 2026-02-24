from django.urls import path
from .views import check
from .views import contact_list,contact_detail

urlpatterns = [
    path('check/',check.as_view()),
    path('contact/',contact_list.as_view()),
    path('contact/<int:pk>',contact_detail.as_view()),
]