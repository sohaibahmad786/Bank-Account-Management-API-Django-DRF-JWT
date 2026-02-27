from django.urls import path
from .views import account_list,account_detail
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('account/',account_list.as_view()),
    path('account/<int:pk>/',account_detail.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
]
