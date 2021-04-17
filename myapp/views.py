from django.shortcuts import render, redirect
from .forms import ProfileForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

def UserProfile(request):
    user_ = request.user
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user_new_info = form.save(commit=False)
            user_.first_name = user_new_info.first_name
            user_.last_name = user_new_info.last_name
            user_.email = user_new_info.email
            if 'image' in request.FILES:
                user_.image = request.FILES['image']
            # user_.image = user_new_info.reques
            user_.description = user_new_info.description
            user_.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'myapp/profile.html', context)


def home(request):
    return render(request, 'myapp/index.html')

