from django.db import models
from django.utils import timezone


# Create your models here.
# 장고 모델에서 클래스 속성은 데이터베이스에서의 '열'을 의미한다

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        # Database의 auth User테이블에 기록되어 있는 값을 참조.
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
