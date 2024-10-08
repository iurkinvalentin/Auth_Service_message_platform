from django.urls import path
from .views import LoginView, LogoutView, RegisterView, DeleteView, ProfileUpdateView, ContactManagementView, ProfileDetailView, VerifyTokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify_token'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-user/', DeleteView.as_view(), name='delete-user'),
    path('update-user/', ProfileUpdateView.as_view(), name='update-user'),
    path('contacts/', ContactManagementView.as_view(), name='contact_management'),
    path('contacts/<int:pk>/', ContactManagementView.as_view(), name='contact_management_detail'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail-id'),
]