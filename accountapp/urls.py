from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [


    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), #import
         name = 'login'),
    path('logout/', LogoutView.as_view(), name= 'logout'),      #import

    path('create/', AccountCreateView.as_view(), name= 'create'),        # AccountCreateView import(연결 라우팅)
    path('detail/<int:pk>', AccountDetailView.as_view(), name= 'detail'),        # import
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),     #import
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete')  #import
]



