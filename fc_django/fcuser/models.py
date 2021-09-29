from django.db import models

# Create your models here.
class Fcuser(models.Model):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(
        max_length=64, verbose_name="패스워드"
    )
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="등록날짜"
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = "factcampus_fcuser"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
