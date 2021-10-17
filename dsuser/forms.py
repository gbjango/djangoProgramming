from django import forms
from .models import Dsuser
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : '아이디를 입력하세요.'
        },
        max_length=64, label='아이디'
    )
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력하세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력하세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '확인 비밀번호를 입력하세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if not(username and email and password and re_password):
            self.add_error('re_password', '모든 값을 입력해야 합니다.')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 다릅니다.')
                self.add_error('re_password', '비밀번호가 다릅니다.')


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : '아이디를 입력하세요.'
        },
        max_length=64, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력하세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                dsuser = Dsuser.objects.get(username=username)
            except Dsuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return

            if not check_password(password, dsuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.username = dsuser.username
