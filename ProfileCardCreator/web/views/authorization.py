from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.views.generic import View
from django.shortcuts import render, redirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        return redirect('custom 403 error')


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Admin_group').exists()

    def handle_no_permission(self):
        return redirect('custom 403 error')


class StuffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Stuff_group').exists()

    def handle_no_permission(self):
        return redirect('custom 403 error')


class AddUserToGroupView(SuperuserRequiredMixin, View):
    template_name = 'authorization/add_user_to_group.html'

    def get(self, request):
        groups = Group.objects.all()
        users = User.objects.all()
        return render(request, self.template_name, {'groups': groups, 'users': users})

    def post(self, request):
        user_id = request.POST.get('user_id')
        group_id = request.POST.get('group_id')

        try:
            user = User.objects.get(pk=user_id)
            group = Group.objects.get(pk=group_id)

            if user.groups.contains(group):
                raise ValueError
            user.groups.add(group)

            return redirect('index')
        except (User.DoesNotExist, Group.DoesNotExist, ValueError):
            error_message = 'Group already added to this user'
            groups = Group.objects.all()
            users = User.objects.all()
            return render(request, self.template_name,
                          {'error_message': error_message, 'groups': groups, 'users': users})


class RemoveUserToGroupView(SuperuserRequiredMixin, View):
    template_name = 'authorization/remove_user_to_group.html'

    def get(self, request):
        groups = Group.objects.all()
        users = User.objects.all()
        return render(request, self.template_name, {'groups': groups, 'users': users})

    def post(self, request):
        user_id = request.POST.get('user_id')
        group_id = request.POST.get('group_id')

        try:
            user = User.objects.get(pk=user_id)
            group = Group.objects.get(pk=group_id)

            if not user.groups.contains(group):
                raise ValueError
            user.groups.remove(group)

            return redirect('index')
        except (User.DoesNotExist, Group.DoesNotExist, ValueError):
            error_message = 'User isn\'t in the specified group'
            groups = Group.objects.all()
            users = User.objects.all()
            return render(request, self.template_name, {'error_message': error_message,'groups': groups, 'users': users})
