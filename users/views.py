from django.views import generic
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class SigupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
