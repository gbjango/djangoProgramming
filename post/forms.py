from django import forms
from .models import Post
from tag.models import Tag

# Create your models here. 작성자, 이미지 주소, 내용, 작성일, 태그

class PostForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력하세요.'
        },
        max_length=128, label='제목'
    )
    image_address = forms.CharField(
        error_messages={
            'required': '이미지 주소를 넣으세요.'
        }, label='이미지 주소'
    )
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력하세요.'
        },
        widget=forms.Textarea, label='내용'
    )
    tags = forms.CharField(
        required=False, label="태그"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        image_address = cleaned_data.get('image_address')
        contents = cleaned_data.get('contents')
        tags = cleaned_data.get('tags')

        if not(title and image_address and contents):
            self.add_error('title', '값이 없습니다.')
            self.add_error('image_address', '값이 없습니다.')
            self.add_error('contents', '값이 없습니다.')