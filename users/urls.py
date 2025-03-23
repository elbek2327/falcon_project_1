from users.views import LoginView, RegisterView, LogoutView

app_name = 'users'

from django.urls import path
# from shop import views
from users import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('logout/', LogoutView.as_view(), name='logout_page')
]