from django.shortcuts import render
from .forms import NameArticleForm
from django.views import View
import requests
class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        form = NameArticleForm()
        return render(request, 'api/index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = NameArticleForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            name = form.cleaned_data['name']
            user = requests.get(f'https://api.github.com/users/{name}/repos').json()
            result = []
            for reposit in user:
                info = {
                    'name':reposit['name'],
                    'url':reposit['html_url'],
                    'stars':reposit['stargazers_count']
                }
                result.append(info)

            return render(request, 'api/reposit.html', {'data':result})

# from django.shortcuts import render, redirect
# from django.views import View
# from .forms import NameArticleForm
# from .tasks import fetch_github_repos  # Import your Celery task

# class CommentArticleView(View):
#     def get(self, request, *args, **kwargs):
#         form = NameArticleForm()
#         return render(request, 'api/index.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = NameArticleForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             task = fetch_github_repos.delay(name)  # Start the Celery task
#             return redirect('processing', task_id=task.id)
#
# def processing(request, task_id):
#     task = fetch_github_repos.AsyncResult(task_id)
#     if task.ready():
#         result = task.result
#         return render(request, 'api/reposit.html', {'data': result})
#     else:
#         return render(request, 'api/processing.html')

