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
