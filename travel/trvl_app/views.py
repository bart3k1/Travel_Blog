from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from trvl_app.forms import (AddUserForm, LoginForm)
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from trvl_app.models import Travel


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "index.html")
        return redirect('login')


class AddUserView(View):
    def get(self, request):
        ctx = {
            'form': AddUserForm,
            'head': "Dodaj użytkownika",
        }
        return render(request, 'add_user_form.html', ctx)

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            email=form.cleaned_data['email'])
            return redirect('login')
        ctx = {
            'form': form,
        }
        return render(request, 'add_user_form.html', ctx)


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        ctx = {
            'form': LoginForm,
            'head': "Zaloguj się",
        }
        return render(request, 'login_form.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            form.add_error(field=None, error='Zły login lub hasło')
        ctx = {
            'form': form,
            'head': "Coś nie wyszło, spróbuj ponownie",
        }
        return render(request, 'login_form.html', ctx)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class TravelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'trvl_app.add_travel'
    model = Travel
    fields = ('topic', 'content',)
    success_url = reverse_lazy('list-travel')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TravelListView(ListView):
    model = Travel


class TravelDetailView(DetailView):
    model = Travel


class TravelUpdateView(UpdateView):
    model = Travel
    fields = ('topic', 'content',)
    success_url = reverse_lazy('list-travel')


class TravelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'trvl_app.add_travel'
    model = Travel
    success_url = reverse_lazy('list-travel')