from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductView.as_view()),
    path('demo', DemoView.as_view()),
    path('filter', ProductByCategoryView.as_view())
]
