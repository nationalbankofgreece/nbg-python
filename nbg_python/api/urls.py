from django.conf.urls import url

from api import views


urlpatterns = [
    url('^api$', views.ProxyView.as_view()),
    url('^$', views.ui_view),
]
