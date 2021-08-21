from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.views import LoginView
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter


#router for studentapi viewset
router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', RegisterView.as_view()),  #register url
    path('login/', LoginView.as_view()),      #login url
    path('logout/', views.LogoutView.as_view()),    #logout url
    path('forgot-password/', PasswordResetView.as_view()), #forgot password
    path('forgot-password-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'), #forgot password confirm url
    path('get-token/', TokenObtainPairView.as_view()),  #get jwt token
    path('refresh-token/', TokenRefreshView.as_view()),  #refresh jwt token
]
