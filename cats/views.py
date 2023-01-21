# ИЗМЕНЯЕМ views.py на Вьюсеры 
# Обновлённый views.py используем
#  универсальный вьюсер Класс ModelViewSet

# В классе, наследующемся от ModelViewSet,
#  обязательно должны быть описаны два поля:
# в поле queryset задаётся выборка объектов
#  модели, с которой будет работать вьюсет;
# в поле serializer_class указывается, какой
#  сериализатор будет применён для валидации и сериализации

# views.py
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

# но мы еще ничего не делалаи с утилсом
