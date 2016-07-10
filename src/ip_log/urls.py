from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ip_log import views
from rest_framework.pagination import LimitOffsetPagination,\
    PageNumberPagination

urlpatterns = [
    url(r'^ip$', views.IPLog.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

PageNumberPagination