from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('^', admin.site.urls),
    #path('admin/', admin.site.urls),
    url(r'^$', views.index), #시작 끝

]
