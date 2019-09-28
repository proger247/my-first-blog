from django.shortcuts import render, get_object_or_404
from .models import Postment
from django.utils import timezone



def post_list(request):
    posts = Postment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})   # {'posts': posts} параметр передаваемый шаблону у

def post_detail(request, pk):
    post = get_object_or_404(Postment, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})