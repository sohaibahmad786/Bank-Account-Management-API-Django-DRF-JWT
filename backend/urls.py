from django.urls import path
from .views import student_list,student_detail
from .views import account_list,account_detail
# from .views import LoginView, ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('student/',student_list.as_view()),
    path('student/<int:pk>/',student_detail.as_view()),
    path('account/',account_list.as_view()),
    path('account/<int:pk>/',account_detail.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
    # path("login/", LoginView.as_view(), name="login"),
    # path("protected/", ProtectedView.as_view(), name="protected"),
]