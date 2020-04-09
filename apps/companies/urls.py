from django.urls import path
from .views import CompanyViewSet



urlpatterns = [
    path('', CompanyViewSet.as_view({'get':'list'}), name='company_list_url'),
    path('<int:pk>/', CompanyViewSet.as_view({'get':'retrieve'}), name='company_detail_url'),
    path('<int:pk>/categories/', CompanyViewSet.as_view({'get':'categories'}), name='company_categories_url'),
    path('<int:pk>/update/', CompanyViewSet.as_view({'put':'update'}), name='company_update_url'),
    path('<int:pk>/orders/', CompanyViewSet.as_view({'get':'orders'}), name='company_orders_url'),
    path('create/', CompanyViewSet.as_view({'post':'create'}), name='company_create_url'),
]


