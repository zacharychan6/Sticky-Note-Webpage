from django.shortcuts import render, get_object_or_404, redirect
from .models import sticky_note
from .forms import StickyForm

# Create your views here.


def sticky_list(request):
    posts = sticky_note.objects.all()
    context = {'posts': posts,
               "page_title": "List of Sticky Notes"
               }
    return render(request, 'posts/sticky_list.html', context)


def sticky_details(request, pk):

    post = get_object_or_404(sticky_note, pk=pk)
    return render(request, 'posts/sticky_details.html', {'post': post})


def sticky_create(request):
    if request.method == 'POST':
        form = StickyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sticky_list')
    else:
        form = StickyForm()
    return render(request, 'posts/sticky_form.html', {'form': form})


def sticky_update(request, pk):

    post = get_object_or_404(sticky_note, pk=pk)
    if request.method == 'POST':
        form = StickyForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return redirect('sticky_list')
    else:
        form = StickyForm(instance=post)
    return render(request, 'posts/sticky_form.html', {'form': form})


def sticky_delete(request, pk):

    post = get_object_or_404(sticky_note, pk=pk)
    post.delete()
    return redirect('sticky_list')
