from django.urls import path
#path django import
from profileapp.views import ProfileCreateView

app_name = 'profileapp'


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')

]