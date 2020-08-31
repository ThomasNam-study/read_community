from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView

from fcuser.forms import LoginForm, RegisterForm
from fcuser.models import Fcuser


def logout(request):
    request.session.clear()

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


class RegisterView(FormView):
    template_name =  'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        fcuser = Fcuser(email=form.data.get("email"), password=make_password(form.data.get("password")),
                        level='user')
        fcuser.save()

        return super().form_valid(form)

# def register(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'register.html', {'form': form})
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         useremail = request.POST.get('useremail', None)
#         re_password = request.POST.get('re-password', None)
#
#         res_data = {}
#
#         if not (username and password and re_password and useremail):
#             res_data['error'] = '모든 값을 입력해야 됩니다.'
#         elif password != re_password:
#             res_data['error'] = '비밀번호가 다릅니다.'
#         else:
#             fcuser = Fcuser(
#                 username=username,
#                 useremail=useremail,
#                 password=make_password(password)
#             )
#
#             fcuser.save()
#
#         return render(request, 'register.html', res_data)
