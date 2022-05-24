from django.urls import path
from. import views


urlpatterns = [
    path('create-account/', views.sign_up, name='create-user'),
    path('sigunp-save/', views.register, name='signup-save'),
    # path('login-save/', views.log_in, name='log-in'),
    path('login/', views.LoginView.as_view(), name='login-save'),
    #path('login-submit/', views.user_login, name='user-login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('products/', views.products, name='products'),
]