from django.conf.urls import url
from form1 import views


urlpatterns=[
    url(r'^$',views.users,name='users')
]