from django.urls import path
from module.apps import EducationalModuleConfig
from module.views import ModuleCreateAPIView, ModulePublishedListAPIView, ModuleListAPIView, ModuleRetrieveAPIView, \
    ModuleUpdateAPIView, ModuleDestroyAPIView

app_name = EducationalModuleConfig.name

urlpatterns = [
    path('create/', ModuleCreateAPIView.as_view(), name='module_create'),
    path('', ModulePublishedListAPIView.as_view(), name='modules'),
    path('all/', ModuleListAPIView.as_view(), name='modules'),
    path('<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module'),
    path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module_update'),
    path('delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module_delete'),
]
