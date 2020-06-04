from django.db import models

# Create your models here.
# Model은 데이터베이스에 저장되는 "데이터"를 의미
# 쉽게 말해 SQL의 DB처리를 이곳에서 한다고 생각!
# 데이터 저장 형태를 설정하는 과정이다
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField('date')

    #admin 글 제목 표시하기 위한 함수
    #내가 작성한 class의 title이 보여지도록 함
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField('date')

    def __str__(self):
        return self.title