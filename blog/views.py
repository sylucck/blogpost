from django.shortcuts import get_object_or_404, render,  redirect
from blog.models import Post, Category, Comment, About, Contact
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
def index(request):

    posts = Post.objects.filter(status=1).order_by('-created_on')
    categories = Category.objects.all()
    about = About.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    context = {
        'users': users,
        'categories':categories,
        'about': about,
       
    }
    return render(request, 'blog/index.html', context)



def blog_category(request, slug):
    

    cate = get_object_or_404(Category, slug=slug)
   
    context = {
        'cate': cate,
        
    }      
    return render(request, 'blog/index_category.html', context)

def index_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
   
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = Comment(
                commenter=form.cleaned_data["commenter"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    
    context = {
        'post':post,
        'comments':comments,
        'form': form,
    }
    return render (request, 'blog/index_details.html', context)

def about(request):
    about = About.objects.all()

    context = {
        'about': about,
    }
    return render(request, 'about.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            name = form.cleaned_data.get('name')
            messages.success(request,f' Hello {name}, Your mail has been Sent')
            return redirect('contactsuccess')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    
    return render(request, 'contact.html', context)

def contactsuccess(request):
    return render(request, 'contactsuccess.html')

    

#Anonymous can't view this page. Hoping to work on it soonest.
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f' Your account has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

def author(request):
    author = Profile.objects.all()
    context = {
        'author':author
    }
    return render(request, 'author.html', context)

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            search= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(search).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
