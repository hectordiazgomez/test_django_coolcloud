from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('subtract/', views.subtract, name='subtract'),
    path('multiply/', views.multiply, name='multiply'),
    path('divide/', views.divide, name='divide'),
    path('solve/', views.solve_equation, name='solve_equation'),
    path('integrate/', views.symbolic_integration, name='symbolic_integration'),
]