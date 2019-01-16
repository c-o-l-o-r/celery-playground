# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep
from random import randint



@shared_task
def add(x, y):
    sleep(randint(1, 20))
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)