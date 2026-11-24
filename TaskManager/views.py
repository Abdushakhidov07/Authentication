from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from django.http import Http404, HttpResponse



def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(
                username = data['username'],
                password = data['password'],    
            )
            user = authenticate(request, username = data['username'], password = data['password'])
            group = Group.objects.get(name = 'Simple')
            user.groups.add(group)
            
            if user is not None:
                login(request, user)
                return redirect("profile")
        else:
            return redirect("registration")
    return render(request, 'registration.html')
    
            
        

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username = data['username'], password = data['password'])
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return redirect("login")
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def create_task(request):
    if request.user.groups.filter(name='Editors').exists():
        if request.method == 'POST':
            data = request.POST
            Task.objects.create(
                    title = data['title'],
                    caption = data['caption'],
                    user_id = request.user
                )
            return redirect("my_task")
    else:
        return redirect('profile')
    return render(request, 'create_task.html')
    

@login_required
def show_task(request):
    if request.user.groups.filter(name='Editors').exists():
        data = request.GET.get('qeury')
        tasks = Task.objects.filter(user_id = request.user)
        if data:
            tasks = tasks.filter(Q(title__icontains=data) | Q(caption__icontains=data))
    else:
        return redirect("profile")

    
    return render(request, 'show_task.html', {"tasks":tasks, "data":data})




@login_required
def show_task_by_id(request, pk):
    tasks = Task.objects.get(pk=pk, user_id = request.user)
    if tasks is None:
        raise Http404()
    return render(request, 'show_task_by_id.html', {"tasks":tasks})




def page_not_found_404(request, exption):
    return render(request, "error.html", status=404)
    


@login_required
def change_status(request, pk):
    task = Task.objects.get(Q(pk=pk) & Q(user_id = request.user))
    if request.method == 'POST':
        data = request.POST.get('status')
        if data not in Task.CHOICES_STATUS:
            return HttpResponse("<h1>ERROR STATUS</h1> ")
        task.status=data
        task.save()
        return redirect("show_task_by_id", pk=pk)

        
    return render(request, "choice_status.html", {"status": Task.CHOICES_STATUS, "task":task})
       
        
        
        
    
    