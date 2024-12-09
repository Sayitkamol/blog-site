from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from skill_app.models import Skill

def getPosts(request):
    template_name = 'post_app/list.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)

def getPost(request, pk):
    template_name = 'post_app/detail.html'
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    tags = post.tags.all()
    print(tags)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.post_id = post.id
            cf.save()
            comment_form = CommentForm()
    context = {'post':post, 'comment_form':comment_form, 'comments':comments, 'tags':tags}
    return render(request=request, template_name=template_name, context=context)

def getPostsByTags(request, tagname):
    filter = True
    posts = Post.objects.filter(tags__name=tagname).all()
    return render(request, 'post_app/list.html', {'posts':posts, 'filter':filter})

def about(request):
    template_name = 'about.html'
    skills = Skill.objects.all()
    context = {'skills':skills}
    return render(request=request, template_name=template_name, context=context)