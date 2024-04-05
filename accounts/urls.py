from accounts import views
from django.urls import path

urlpatterns = [
    path('signupaccount/', views.signupaccount, # зарегистрироваться
        name='signupaccont'),
    path('logout/', views.logoutaccount, # выйти из акка
        name='logoutaccount'),
    path('login/', views.loginaccount, # зайти в акк
        name='loginaccount'),
]