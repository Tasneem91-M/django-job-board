from django.urls import include ,path
from .import views

urlpatterns = [
    path('jobs/',views.job_list()),
    path('<int:id>',views.job_detail()),
]
