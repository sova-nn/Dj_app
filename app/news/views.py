from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView
from .models import Article
from .forms import SetMeForm, QuesForm


class NewsView(DetailView):

    model = Article
    template_name = 'article.html'
    context_object_name = 'article'


def show_news(request, myid=0):
    return render(request, 'blabla.html', {"news_id":myid})

class ArticleList(ListView):
    template_name = 'list.html'
    model = Article

    def dispatch(self, request, *args, **kwargs):
        self.form = SetMeForm(request.GET)
        self.form.is_valid()
        self.gform = QuesForm(request.POST or None)
        return super(ArticleList, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        queryset = Article.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        else:
            queryset = queryset.order_by('title', )[:5]
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['gform'] = self.gform
        return context
