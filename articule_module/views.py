from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import DetailView, ListView

from articule_module.models import ArticleCategory, Article, ArticleComment




class ArticleCategories(View):
    def get(self, request):
        article = Article.objects.filter(is_active=True)
        category = ArticleCategory.objects.filter(is_active=True, parent_id=None)

        context = {
            'article': article,
            'category': category
        }
        return render(request, 'articlule_module/article_category.html', context)


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articlule_module/article_datail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comment'] = ArticleComment.objects.filter(article_id=article.id, parent=None).prefetch_related(
            'articlecomment_set')
        return context


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        print(article_id, article_comment, parent_id)
        new_comment = ArticleComment(article_id=article_id, text=article_comment, user_id=request.user.id,
                                     parent_id=parent_id)
        new_comment.save()

    return HttpResponse('response')
