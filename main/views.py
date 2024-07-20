
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignupForm, CommentForm, RatingForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import logout


User = get_user_model()
def home(request):
    return render(request, 'Home.html')

def login_view(request):
    if request.method == 'POST':
        User = get_user_model()
      
        
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
                print(f"User found: {user}")
                print(f"Password check: {user.check_password(password)}")
            except User.DoesNotExist:
                print(f"No user found with email: {email}")
                user = authenticate(request, email=email, password=password)
                print("user", user)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = LoginForm()
    
    return render(request, 'Login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        print("1")
        if form.is_valid():
            print("form", form)
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the 'home' page after successful signup
        else:
            # Debug: Print form errors to the console for inspection
            print(form.errors)

    else:
        form = SignupForm()
    
    return render(request, 'Signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


@require_POST
def add_comment(request):
    if request.method == 'POST':
        print(request.POST)  # Print POST data to console for debugging

        form = CommentForm(request.POST)
        comment_text = request.POST.get('comments', '')  # Retrieve 'comments' from POST data
        rating = request.POST.get('rating', '')
        print("ppppppp", form)
        print("admin", request.user.id)
        user = User.objects.get(id=request.user.id)
        
        if user:
            if form.is_valid():

                comment = form.save(commit=False)
                comment.author = user
                comment.save()
                return JsonResponse({'status': 'success', 'message': 'Comment added successfully'})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        else:
            return JsonResponse({'status': 'error', 'message': 'Comment cannot be empty'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)


def add_rating(request, post_id):
    rating = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            # rating.author = request.user  # Assuming user is authenticated
            rating.save()
            return redirect('home')

    else:
        form = RatingForm()
    
    return render(request, 'home.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout (if needed)
    return redirect('home')  # Replace 'home' with the URL name of your homepage