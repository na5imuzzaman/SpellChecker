from django.urls import path, include
from checking import views as v


urlpatterns = [
    path('', v.text_views, name="text"),

    path('result/', v.result_views, name='result'),
]
