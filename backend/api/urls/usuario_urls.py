from django.urls import path

from api.views import user_views as views

urlpatterns = [
    path('registrar/', views.registerUser, name='registrar'),
    path('perfil/', views.getUserProfile, name='perfil'),
    path('perfil/atualizar/', views.updateUserProfile, name='atualizar_perfil'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('deletar/<str:pk>', views.deleteUser, name='deletar'),
]
