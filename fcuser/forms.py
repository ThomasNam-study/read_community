from django import forms
from django.contrib.auth.hashers import check_password, make_password

from fcuser.models import Fcuser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름", error_messages={
        'required': '아이디를 입력해주세요'
    })
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput, error_messages={
        'required': '비밀번호를 입력해주세요'
    })

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)

                if not check_password(password, fcuser.password):
                    self.add_error("password", '비밀번호가 틀립니다.')
                else:
                    print(fcuser.id)
                    self.user_id = fcuser.id
            except Fcuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')


class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '사용자 이름을 입력해주세요'
        },
        label='사용자 이름',
    )

    useremail = forms.EmailField(
        error_messages={
            'required': '사용자 이메일을 입력해주세요'
        },
        label='사용자 이메일',
    )

    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput, error_messages={
        'required': '비밀번호를 입력해주세요'
    })

    re_password = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput, error_messages={
        'required': '비밀번호를 입력해주세요'
    })

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        # username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if re_password and password and re_password == password:
            username = cleaned_data.get("username")
            useremail = cleaned_data.get("useremail")

            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()

        else:
            self.add_error('password', '패스워드가 다릅니다..')
