# Обновлённый urls.py для views.py на Вьюсерах

# При работе с view-классами и дженериками каждый
#  эндпоинт отдельно описывается в urls.py.
#   Но для вьюсетов есть более удобный и
#    экономичный инструмент — роутеры (англ. routers).

# С помощью роутера для заданных вьюсетов
#  создаются эндпоинты по маске адреса:

# URL-префикс/ и
# URL-префикс/<int:pk>.

# В DRF есть два стандартных роутера:
#  SimpleRouter и DefaultRouter. Они очень похожи, начнём с первого.

from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]

# Этот роутер сгенерирует два эндпоинта:
# cats/,
# cats/<int:pk>/.

# # !!!!!!!!!!!!!!!!!!!!!! 
# # тоже самое через роутер router = DefaultRouter() 
# # # # DefaultRouter — это расширенная версия SimpleRouter:
# # # #  он умеет всё то же, что и SimpleRouter,
# # # #  а в дополнение ко всему генерирует корневой эндпоинт /,
# # # #  GET-запрос к которому вернёт список ссылок на все ресурсы, доcтупные в API. 


# from django.urls import include, path

# from rest_framework.routers import DefaultRouter

# from cats.views import CatViewSet


# router = DefaultRouter()
# router.register('cats', CatViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
