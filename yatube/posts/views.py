from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .models import Post, Group, get_user_model

from .forms import PostForm

from django.contrib.auth.decorators import login_required

User = get_user_model()

NUM_OF_OBJ = 10


def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    title = 'Последние обновления на сайте'
    paginator = Paginator(posts, NUM_OF_OBJ)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, NUM_OF_OBJ)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    description = ''
    title = f'Записи сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
        'description': description,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    sum_of_posts = posts.count()
    paginator = Paginator(posts, NUM_OF_OBJ)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
        'sum_of_posts': sum_of_posts,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    pub_date = post.pub_date
    sum_of_posts = author.posts.count()
    context = {
        'author': author,
        'post': post,
        'pub_date': pub_date,
        'sum_of_posts': sum_of_posts,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', username=request.user.username)
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        if request.user == post.author:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.save()
                return redirect('posts:post_detail', post_id=post_id)
        return render(
            request, 'posts/create_post.html', {
                'form': form, 'is_edit': True})
    if request.method == "GET":
        if request.user == post.author:
            form = PostForm(instance=post)
        else:
            return redirect('posts:post_detail', post_id=post_id)
        return render(
            request, 'posts/create_post.html', {
                'form': form, 'is_edit': True})
