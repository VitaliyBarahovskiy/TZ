from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Prob(models.Model):
    number = models.CharField(verbose_name='Название', db_index=True, max_length=64)
    sotrudnik = models.CharField(verbose_name='Сотрудник', max_length=64)
    dolznoct = models.CharField(verbose_name='Должность', max_length=64)
    company_type = models.CharField(verbose_name='Тип компаний', max_length=64)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)