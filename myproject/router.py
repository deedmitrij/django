from rest_framework import routers
from test_project.viewsets import EmployeeViewSet, MeasurementViewSet


router = routers.DefaultRouter()
router.register(r'participant', EmployeeViewSet)
router.register(r'measurement', MeasurementViewSet)
