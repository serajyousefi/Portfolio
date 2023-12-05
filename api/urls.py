from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('usercreate/', views.UserCreate.as_view()),
    path('userread/', views.UserRead.as_view()),
    path('searchuserbyid/<int:id>', views.SearchUserById.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
