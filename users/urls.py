from django.urls import path
from users.views import (
    login_view,
    RegisterView,
    logout_request
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_request, name='logout'),
]
