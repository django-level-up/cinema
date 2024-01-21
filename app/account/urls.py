from django.urls import path
from .views import Greeting

app_name = "account"

urlpatterns = [path("", Greeting.as_view(), name="greeting")]
