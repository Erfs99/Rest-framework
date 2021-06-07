from django.urls import path
from .views import registration,ListOfAccounts,single_account,update_account
app_name="accounts"
urlpatterns=[
    path("api/register",registration,name="register"),
    path("api/all",ListOfAccounts,name="list_all"),
    path("api/update/<pk>",update_account),
    path("api/single/<pk>",single_account,name="single_account"),
    
]
