from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleCategories.as_view(), name='article_list'),
    path('<pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('add-article-comment', views.add_article_comment, name='add_article_comment')

]
