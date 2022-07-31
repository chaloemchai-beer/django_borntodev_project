from django.urls import path
from .views import index,blogDetail,resultdata

urlpatterns = [
    path('', index, name='index'),
    path('blog/<int:id>', blogDetail, name='blogDetail'),
    path('<int:category_id>/', resultdata, name='resultdata'),
]
