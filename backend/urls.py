from django.urls import path
from .views import student_list,student_detail


urlpatterns = [
    path('student/',student_list.as_view()),
    path('student/<int:pk>/',student_detail.as_view()),
]