from rest_framework import routers
from . import views

app_name = 'catalogues'
router = routers.DefaultRouter(trailing_slash=False)

router.register(
    r'users',
    views.UserView,
    'users'
)
router.register(
    r'cars',
    views.CarView,
    'cars'
)

urlpatterns = [

]

urlpatterns += router.urls
