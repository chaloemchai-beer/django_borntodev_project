import imp
from unicodedata import category
from django.shortcuts import render
from category.models import Category
from email_manage.models import Email
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()

    latest = Blogs.objects.all().order_by('-pk')[:4]
    latest_h = Blogs.objects.all().order_by('-pk')[:1]

    popular_h = Blogs.objects.all().order_by('-views')[:1]
    popular = Blogs.objects.all().order_by('-views')[:4]

    recommend = Blogs.objects.all().order_by('views')[:4]
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

    data = {
        'categories': categories,
        'blogs': blogPerpage,
        'latest': latest,
        'latest_h': latest_h,
        'popular_h': popular_h,
        'popular': popular,
        'recommend': recommend,
        'recommend_h': recommend_h,
    }

    return render(request, 'index.html', data)


def resultdata(request, category_id):
    results = Blogs.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    recommend = Blogs.objects.all().order_by('views')[:4]
    popular = Blogs.objects.all().order_by('-views')[:4]

    data = {
        'results': results, 
        'categories': categories,
        'recommend':recommend,
        'popular':popular
        }

    return render(request, 'result.html', data)


def blogDetail(request, id):
    recommend = Blogs.objects.all().order_by('views')[:4]
    popular = Blogs.objects.all().order_by('-views')[:4]
    categories = Category.objects.all()

    singleBlog = Blogs.objects.get(id=id)
    singleBlog.views = singleBlog.views+1
    singleBlog.save()

    data = {
        'blog': singleBlog,
        'popular': popular,
        'recommend': recommend,
        'categories':categories,
    }

    return render(request, 'blogDetail.html', data)

def post_email(request) :
    
    return render(request, 'index.html',{'email':email})
