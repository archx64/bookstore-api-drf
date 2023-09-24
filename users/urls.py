from django.urls import path
from users.views import SigupPageView

urlpatterns=[
path('signup/', SigupPageView.as_view(), name='signup')
]