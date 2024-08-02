from django.urls import path
from . import views
app_name = 'tasks'

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView  #agregado
from django.contrib.auth.forms import UserCreationForm #agregado

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:task_id>', views.detail, name='detail'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('signup/', views.UserCreateAndLoginView.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='tasks/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(),
         name='password_change_done'),
    path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    
]
