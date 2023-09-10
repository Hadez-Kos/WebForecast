from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(
        verbose_name='Email адрес', max_length=255, unique=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=150, blank=False
    )
    first_name = models.CharField(
        verbose_name='Имя', max_length=150, blank=False
    )
    middle_name = models.CharField(
        verbose_name='Отчество', max_length=150, blank=True
    )
    phone = models.CharField(
        verbose_name='Телефон', max_length=20, blank=False
    )
    birthday = models.DateField(
        verbose_name='Дата рождения', blank=False
    )
    password = models.CharField(
        verbose_name='Пароль', max_length=200, blank=False
    )

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __repr__(self):
        return f"{self.full_name} {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class ProfessionChoices(models.Model):
    profession = models.CharField(
        verbose_name='Профессия', max_length=150, blank=False
    )
    position = models.CharField(
        verbose_name='Должность', max_length=150, blank=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __repr__(self):
        return f"{self.profession} {self.position}"

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
