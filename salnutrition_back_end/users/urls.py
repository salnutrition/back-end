from django.urls import path
from .views import RegisterView, LoginView, LogoutView, MeView, UpdateProfilePictureView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("me/", MeView.as_view()),
    path("upload-profile-picture/", UpdateProfilePictureView.as_view()),
    #path("update-bio/", UpdateBioView.as_view()),
]