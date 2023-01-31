from django.urls import path
from . import views
from .views import logout_view
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("department/", views.department, name="department"),
    path("doctors/", views.doctors, name="doctors"),
    # path('profile/', views.profile, name='profile'),
    # path("update_profile/<int:pk>", views.update_profile, name="update_profile"),
    path("signup/", views.signup, name="signup"),
    path(
        "create_patient/",
        views.CreatePatientView.as_view(),
        name="create_patient",
    ),
    path(
        "login/",
        views.UserLoginView.as_view(),
        name="login_patient",
    ),
    path('logout/', logout_view, name='logout'),
   

]
