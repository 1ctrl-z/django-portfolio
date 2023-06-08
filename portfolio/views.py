from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
    """
    This function registers a user by creating a form and saving the user's information if the form is
    valid.
    
    :param: The request object represents the HTTP request that the user made to the server. It contains information about the request, such as the HTTP method used (GET, POST, etc.), the URL requested, and any data submitted in the request
    :return: The function `register` returns a rendered HTML template `register.html` with a `UserCreationForm` object passed as context if the request method is GET. If the request method is POST and the form is valid, the function redirects to the `home` URL. If the form is not valid, the same HTML template with the invalid form is returned.
    """
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})

@login_required()
def home_view(request):
    """
    This is a Python function that returns a rendered HTML template called "index.html" for a home view.
    
    :param: The request parameter is an object that represents the HTTP request made by the client to the server. It contains information such as the HTTP method used (GET, POST, etc.), the headers, the query parameters, and the body of the request. It is passed as the first argument to Django views
    :return: The `home_view` function is returning an HTTP response that renders the `index.html` template using the `render` function.
    """
    return render(request, 'index.html')