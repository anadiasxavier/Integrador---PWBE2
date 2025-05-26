from django.urls import path 
from .views import SensoresListCreate , SensoresRetrieveUpdateDestroy, AmbientesListCreate, AmbientesRetrieveUpdateDestroy , HistoricoListCreate, HistoricoRetrieveUpdateDestroy
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #Sensores 
    path('sensores/', SensoresListCreate.as_view()),
    path('sensores/<int:pk>/', SensoresRetrieveUpdateDestroy.as_view()),

    #Ambientes 
    path('ambientes/', AmbientesListCreate.as_view()),
    path('ambientes/<int:pk>/', AmbientesRetrieveUpdateDestroy.as_view()),

    #Historico
    path('historico/', HistoricoListCreate.as_view()),
    path('historico/<int:pk>/', HistoricoRetrieveUpdateDestroy.as_view()),

    #Login
    path('login/',TokenObtainPairView.as_view()),
]
#ana
#24240109