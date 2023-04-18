from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from . models import Authors,Pub_house,Books
from django.template import loader
from .forms import AuthorsForm,Pub_houseForm,BooksForm
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse


def index(request):
    books = Books.objects.all()
    context = {

        'books': books,
        'title':'Главная'
    }
    return render(request, 'main/index.html',context)

def view_a(request):
    books = Authors.objects.all()
    context = {
        'authors': books,
        'title':'Посмотреть'
    }
    return render(request, 'main/view_a.html',context)

def view_b(request):
    books = Books.objects.all()
    context = {
        'books': books,
        'title':'Посмотреть'
    }
    return render(request, 'main/view_b.html',context)

def view_ph(request):
    ph = Pub_house.objects.all()
    context = {
        'ph': ph,
        'title':'Посмотреть'
    }
    return render(request, 'main/view_ph.html',context)

def create_a(request):
    authors = Authors.objects.all()
    error=""
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="form is uncorrect"

    form=AuthorsForm()
    context={
        'form':form,
        'authors':authors,
        'error':error
    }
    return render(request, 'main/create_a.html',context)

def create_pb(request):
    ph = Pub_house.objects.all()
    error=""
    if request.method == 'POST':
        form = Pub_houseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="form is uncorrect"

    form=Pub_houseForm()
    context={
        'form':form,
        'error':error,
        'pub_house':ph
    }
    return render(request, 'main/create_pb.html',context)

def create_b(request):
    error=""
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="form is uncorrect"

    form=BooksForm()
    context={
        'form':form,
        'error':error
    }
    return render(request, 'main/create_b.html',context)


def update(request, id):
  books = Books.objects.get(id=id)
  context = {
    'book': books,
  }
  return render(request, 'main/update.html', context)

def updaterecord(request, id):
  name = request.POST['name']
  num_page = request.POST['num_page']
  seria = request.POST['seria']
  id_a = request.POST['id_a']
  id_ph = request.POST['id_ph']

  book = Books.objects.get(id=id)

  book.name=name
  book.num_page=num_page
  book.seria=seria
  book.id_a=get_object_or_404(Authors, surname=request.POST['id_a'])
  book.id_ph=get_object_or_404(Pub_house, name=request.POST['id_ph'])
  book.save()
  return HttpResponseRedirect(reverse('home'))


def view_edit(request, id):
    template = loader.get_template('main/update.html')
    book = get_object_or_404(Books, pk=id)
    context = {
        'book': book,
        'authors':Authors.objects.all(),
        'ph': Pub_house.objects.all()
    }
    if all(['id_a' in request.POST, 'id_ph' in request.POST, 'name' in request.POST, 'num_page' in request.POST, 'seria' in request.POST]):
        book.id_a = get_object_or_404(Authors, pk=request.POST['id_a'])
        book.id_ph = get_object_or_404(Pub_house, pk=request.POST['id_ph'])

        book.name = request.POST['name']
        book.seria = request.POST['seria']
        book.num_page = request.POST['num_page']
        book.save()
    return HttpResponse(template.render(context, request))