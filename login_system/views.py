from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class UserFormView(View):
    """ UserFormView creates a view to allow users to register"""
    form_class = UserForm
    sign_up = 'login_system/sign_up.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.sign_up, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('index')
