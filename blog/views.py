from django.shortcuts import render
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage

categories = Category.objects.all()
recommend = Blogs.objects.all().order_by('views')[:4]
popular = Blogs.objects.all().order_by('-views')[:4]


def index(request):
    blogs = Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:4]
    latest_h = Blogs.objects.all().order_by('-pk')[:1]
    popular_h = Blogs.objects.all().order_by('-views')[:1]
    recommend_h = Blogs.objects.all().order_by('views')[:1]

    # pagination
    paginator = Paginator(blogs, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        blogPerpage = paginator.page(page)
    except(EmptyPage, InvalidPage):
        blogPerpage = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'blogs': blogPerpage,
        'latest': latest,
        'latest_h': latest_h,
        'popular_h': popular_h,
        'popular': popular,
        'recommend': recommend,
        'recommend_h': recommend_h,
    }

    return render(request, 'index.html', context)


def resultdata(request, category_id):
    results = Blogs.objects.filter(category_id=category_id)

    context = {
        'results': results,
        'categories': categories,
        'recommend': recommend,
        'popular': popular
    }

    return render(request, 'result.html', context)


def blogDetail(request, id):
    singleBlog = Blogs.objects.get(id=id)
    singleBlog.views = singleBlog.views+1
    singleBlog.save()

    context = {
        'blog': singleBlog,
        'popular': popular,
        'recommend': recommend,
        'categories': categories,
    }

    return render(request, 'blogDetail.html', context)
