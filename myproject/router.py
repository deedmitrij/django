from rest_framework import routers
from test_project.viewsets import EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'participant', EmployeeViewSet)
