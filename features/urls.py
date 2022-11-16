from django.urls import path
from. import views

urlpatterns = [
	path('',views.home, name='home'),
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'), 
	path('success/<auth_token>', views.success, name='success'),

	path('dashboard/', views.dashboard, name='dashboard'),

	
]