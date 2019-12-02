from django.shortcuts import render,HttpResponse

# Create your views here.


def HomePage(request):

    if request.user.is_authenticated:
        print(request.user)
        content={
            'isim':'Melih'
        }
    else:
        content={
            'isim' : 'Misafir'
        }

    return render(request ,"home.html", content)