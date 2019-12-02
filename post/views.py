from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from django.db import models
from .models import Posts
from .forms import FormPost,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


     

def postIndex(request):

    post_list=Posts.objects.all()
    query=request.GET.get("arama")
    if query:
        post_list=post_list.filter( 
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(users__first_name__icontains=query) |
            Q(users__last_name__icontains=query)
        )

    paginator = Paginator(post_list, 8) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)







    content={
        'postdata':contacts
    }

    return render(request,'post/index.html',content)


def postDetail(request,pk):

    postDetail2=get_object_or_404(Posts, pk=pk)

    forms=CommentForm(request.POST or None) 
    if forms.is_valid():
        comments=forms.save(commit=False)
        comments.post=postDetail2
        comments.save()
        messages.success(request,"Başarılı bir şekilde eklediniz  ",extra_tags="add")
        return HttpResponseRedirect(postDetail2.get_absolute_url())


    content={
        'posdetailpage':postDetail2,
        'forms':forms,
    }

    return render(request,'post/detail.html',content)


def post_create(request):
# if not request.user.is_authenticated():
#    return Http404()
    form=FormPost(request.POST or None , request.FILES or None) 
    if form.is_valid():
        postcre=form.save(commit=False)
        postcre.users=request.user
        postcre.save()
        messages.success(request,"Başarılı bir şekilde eklediniz  ",extra_tags="add")
        return HttpResponseRedirect(postcre.get_absolute_url())

    
    content={
        'formsend':form
    }
   
    return render(request,"post/form.html", content)


def postUpdate(request, pk):
    postDetail2=get_object_or_404(Posts, pk=pk)
    form=FormPost(request.POST or None, request.FILES or None ,instance=postDetail2)
    if form.is_valid():
        form.save()
        messages.success(request,"Başarılı şekilde güncellendi  ",extra_tags="update")
        return HttpResponseRedirect(postDetail2.get_absolute_url())

    content={
        'formsend':form
    }


    return render(request,"post/form.html", content)



def postDelete(request,pk):
    postDetail2=get_object_or_404(Posts, pk=pk)
    postDetail2.delete()
    return redirect('anasayfa')



