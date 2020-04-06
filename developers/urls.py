from django.conf.urls import url
from . import views

app_name='developers'
urlpatterns = [
    url(r'^signup/',views.signup_view,name='signup'),
    url(r'^login/',views.login_view,name="login"),
]