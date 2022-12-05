from django.shortcuts import render, HttpResponse
from postApp import forms

posts = []


def show_all(request):
    return render(request, 'all.html',
                  {'posts': posts})


def add_new(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        content = request.POST.get('content')
        is_publish = request.POST.get('is_publish')
        date = request.POST.get('date')
        post = {}
        post['header'] = header
        post['content'] = content
        post['date'] = date
        if not is_publish:
            return HttpResponse('<h2>Пост не был опубликован</h2>')
        posts.append(post)
        return HttpResponse(f"<h2>Пост добавлен под номером {len(posts)}</h2>")
    else:
        post = forms.PostForm()
    return render(request, 'add_new.html', {'form': post})
