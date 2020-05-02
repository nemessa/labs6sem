from django.db import models
from django.utils import timezone
from random import randint


class Client(models.Model):
    name = models.CharField('name', max_length=32)
    family = models.CharField('family', max_length=32)
    patronymic = models.CharField('patronymic', max_length=32, blank=True)
    age = models.DateTimeField()
    login = models.CharField('login', max_length=32, unique=True)
    password = models.CharField('password', max_length=32)

    def __repr__(self):
        return '<Object Client: id = {}, name = {}, login = {}>'.format(self.id,
                                                                        self.name,
                                                                        self.login)


class Account(models.Model):
    number = models.CharField('name',
                              max_length=32,
                              default=str(randint(100000000, 999999999)),
                              unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    date_open = models.DateTimeField(default=timezone.now())

    def __repr__(self):
        return '<Object Account: id = {}, number = {}, balance = {}>'.format(self.id,
                                                                             self.number,
                                                                             self.balance)
