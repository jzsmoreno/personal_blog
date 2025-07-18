from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("blogs:home_page")

    context = {"form": form}
    return render(request, "registration/register.html", context)
