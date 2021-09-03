from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('register/', views.reigsterPage, name='register'),
	path('logout/', views.logoutUser, name='logout'),
	path('login/', views.loginPage, name='login'),
	path('clientpage/', views.clientPage, name='clientpage'),
	path('profile/', views.profile, name='profile'),
	path('deposit/', views.deposit, name='deposit'),
	path('withdrawl/', views.withdrawl, name='withdrawl'),
	path('transactions/', views.transactions, name='transactions'),
	path('groupPage/', views.groupPage, name='groupPage'),
	path('createClient/', views.createClient, name='createClient'),
	path('editClient/<str:pk>/', views.editClient, name='editClient'),
	path('deleteClient/<str:pk>/', views.deleteClient, name='deleteClient'),
	path('createDeposit/', views.createDeposit, name='createDeposit'),
	path('deleteDeposit/<str:pk>/', views.deleteDeposit, name='deleteDeposit'),
	path('createWithdraw/', views.createWithdraw, name='createWithdraw'),
	path('deleteWithdrawl/<str:pk>/', views.deleteWithdrawl, name='deleteWithdrawl'),
	path('createGroup/', views.createGroup, name='createGroup'),
	path('deleteGroup/<str:pk>/', views.deleteGroup, name='deleteGroup'),

	


	
	
	
	
	


]