from django import forms
from django.contrib.auth.hashers import check_password

from fcuser.models import Fcuser


class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label="제목", error_messages={
        'required': '제목을 입력해주세요'
    })
    contents = forms.CharField(label="내용", widget=forms.Textarea, error_messages={
        'required': '비밀번호를 입력해주세요'
    })
