from rest_framework import routers
from . import views

app_name = 'control'
router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [

]

urlpatterns += router.urls