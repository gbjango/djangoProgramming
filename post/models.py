from django.db import models

# Create your models here. 작성자, 이미지 주소, 내용, 작성일, 태그

class Post(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    writer = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE, verbose_name='작성자')
    image_address = models.CharField(max_length=600, verbose_name='이미지주소')
    contents = models.TextField(verbose_name='내용')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
  

    def __str__(self):
        return self.image_address

    class Meta:
        db_table = 'jangostar_post'
        verbose_name = '장고스타그램 게시글'
        verbose_name_plural = '장고스타그램 게시글'