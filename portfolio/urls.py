from django.urls import path,include

urlpatterns = [
   path('portfolio/api/', include('api.urls'))
]


