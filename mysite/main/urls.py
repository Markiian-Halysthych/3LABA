from django.urls import path
from . import views

urlpatterns= [
    path('', views.view_page, name='view'),
    path('create_page',views.create_page, name='create'),
    path('<int:pk>/update', views.CarUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.CarDeleteView.as_view(), name='delete')
]