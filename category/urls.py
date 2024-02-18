from django.urls import path
from .apps import CategoryConfig
from .views import CategoryCreateAPIView, CategoryListAPIView, CategoryRetrieveAPIView, CategoryUpdateAPIView, \
    CategoryDestroyAPIView

app_name = CategoryConfig.name

urlpatterns = [
    path('create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('', CategoryListAPIView.as_view(), name='categories'),
    path('<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category'),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='modules_update'),
    path('delete/<int:pk>/', CategoryDestroyAPIView.as_view(), name='modules_delete'),
]
