from django.shortcuts import render, get_object_or_404, redirect
from .models import Buku
from .forms import BukuForm

# Create your views here.

def buku_list(request):
    bukus = Buku.objects.all()
    return render(request, 'books/buku_list.html', {'bukus': bukus})

def buku_create(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buku_list')
    else:
        form = BukuForm()
    return render(request, 'books/buku_form.html', {'form': form})

def buku_update(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('buku_list')
    else:
        form = BukuForm(instance=buku)
    return render(request, 'books/buku_form.html', {'form': form})

def buku_delete(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    if request.method == 'POST':
        buku.delete()
        return redirect('buku_list')
    return render(request, 'books/buku_confirm_delete.html', {'buku': buku})
