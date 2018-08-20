from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from .forms import User_Form


class IndexView(generic.View):
    def get(self, request):
        return HttpResponse("ACCOUNTS!")

class UserRegisterView(generic.View):
    form_class = User_Form
    template_name = 'accounts/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)#None is context. Now form will not be pre filled.
        return render(request, self.template_name, {'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST) #Now the form is filled with the user data submitted by unknown

        if form.is_valid():
            user = form.save(commit=False)

            #clean normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('accounts:index')

        else:
            return render(request, self.template_name, {'form': form})

class UserLoginView(generic.View):
    template_name = 'accounts/login_form.html'
    form_class = AuthenticationForm

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:index')

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})



