from django.urls import path
from .views import CategoryViewSet



urlpatterns = [
    path('', CategoryViewSet.as_view({'get':'list'}), name='category_list_url'),
    path('<int:pk>/', CategoryViewSet.as_view({'get':'retrieve'}), name='category_detail_url'),
    path('<int:pk>/update/', CategoryViewSet.as_view({'put':'update'}), name='category_update_url'),
    path('<int:pk>/delete/', CategoryViewSet.as_view({'delete':'destroy'}), name='category_update_url'),
    path('create/', CategoryViewSet.as_view({'post':'create'}), name='category_create_url'),
]


