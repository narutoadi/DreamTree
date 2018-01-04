from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .forms import addDreamForm
from .models import Dream


def post_dream(request):
    if request.method == "POST":
        form = addDreamForm(request.POST)
        if form.is_valid():
            post = form.save(request.POST)
            post.save()
            return redirect('/')
    else:
        form = addDreamForm()
        return render(request, 'manageDreams\post_dream.html',{'form': form})

def show_dream(request):
    try:
        allDreams = Dream.objects.all()
    except Dream.DoesNotExist:
        raise Http404("No dream exists")
    return render(request, 'manageDreams/show_dream.html', {'allDreams': allDreams})

def done_with_dream(request):
    return render(request, 'manageDreams/done_with_dream.html',{})

