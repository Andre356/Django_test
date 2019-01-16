from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, User
from .forms import UserForm, GroupForm

from rest_framework import viewsets
from .serializers import MyGroupsSerializer, MyUsersSerializer


class MyGroupsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows db groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = MyGroupsSerializer


class MyUsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows db users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = MyUsersSerializer


def home(request):
    groups_list = Group.objects.all()
    users_list = User.objects.all()
    return render(request, 'main/home.html', {'grupy': groups_list, 'uzytkownicy': users_list})


def new_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'main/new_user.html', {'form': form})


def new_group(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'main/new_group.html', {'form': form})


def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'main/new_user.html', {'form': form})


def edit_group(request, id):
    group = get_object_or_404(Group, pk=id)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'main/new_group.html', {'form': form})


def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect(home)
    return render(request, 'main/confirm.html', {'user': user})


def delete_group(request, id):
    group = get_object_or_404(Group, pk=id)
    if request.method == 'POST':
        group.delete()
        return redirect(home)
    return render(request, 'main/confirm.html', {'group': group})
