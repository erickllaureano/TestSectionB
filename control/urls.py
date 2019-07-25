from rest_framework import routers
from . import views

app_name = 'control'
router = routers.DefaultRouter(trailing_slash=False)

router.register(
    r'assigned_car',
    views.AssignedCarsView,
    'assigned_car'
)
router.register(
    r'used_car',
    views.UsedCarsView,
    'used_car'
)

urlpatterns = [

]

urlpatterns += router.urls