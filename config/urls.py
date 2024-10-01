"""
Конфигурация URL для проекта конфигурации.

Список `urlpatterns` направляет URL к представлениям. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Примеры:
Виды функций
1. Добавьте импорт: from my_app import views
2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Виды на основе классов
1. Добавьте импорт: from other_app.views import Home
2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
1. Импортируйте функцию include(): from django.urls import include, path
2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
