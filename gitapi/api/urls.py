from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentArticleView.as_view(), name='test'),
    # path('processing/<str:task_id>/', views.processing, name='processing'),
]