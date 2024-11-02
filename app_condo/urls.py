from django.urls import path
from . import views

app_name = 'app_condo'  # App namespace

urlpatterns = [
    path('', views.predict, name='predict'),  # Predict page
    path('explore/', views.explore_view, name='explore'),
    path('loan_table/', views.loan_table_view, name='loan_table'),
    path('get-subdistricts/<int:district_id>/', views.get_subdistricts, name='get_subdistricts'),
    path('get-nearest-roads/<int:subdistrict_id>/', views.get_nearest_roads, name='get_nearest_roads'),
]
