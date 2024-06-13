from django.urls import path
from . import views
from .views import api_example
from .views import LoginView
from .views import get_weasis_url
from .views import DashboardStatsView
from .views import PatientRecordsView
from .views import DICOMImageUploadView


urlpatterns = [
  path('api/auth/login/', LoginView.as_view(), name='login'),
  path('api/example/', api_example, name='api_example'),
  path('', views.home, name='home'),
  path('patients/', views.patient_list, name='patient_list'),
  path('upload/', DICOMImageUploadView.as_view(), name='dicom-upload'),
  path('weasis/<int:dicom_id>/', get_weasis_url, name='weasis-url'),
  path('api/dashboard/stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
  path('api/patients/', PatientRecordsView.as_view(), name='patient-records'),

]
