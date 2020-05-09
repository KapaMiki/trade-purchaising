from django.urls import path
from .views import ProductViewSet



urlpatterns = [
    path('', ProductViewSet.as_view({'get':'list'}), name='product_list_url'),
    path('<int:pk>/', ProductViewSet.as_view({'get':'retrieve'}), name='product_detail_url'),
    path('create/', ProductViewSet.as_view({'post':'create'}), name='product_create_url'),
    path('<int:pk>/update/', ProductViewSet.as_view({'put':'update'}), name='product_update_url')
]


