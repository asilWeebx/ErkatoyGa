from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app.form import CreateUserForm
from app.models import Product, Category


class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return Product.objects.filter(title__icontains=title)
        return Product.objects.all()


def about(request):
    return render(request, 'about.html')


@ login_required
def sevimli(request):
    new = Product.objects.filter(favourites=request.user)
    return render(request, 'sevimli.html', {'new': new})


# class DetailsView(DetailView):
#     model = Product
#     template_name = 'details.html'
#     queryset = Product.objects.all()


def details(request, pk):
    products = Product.objects.order_by('-id')
    product = Product.objects.filter(id=pk).last()

    fav = bool

    if product.favourites.filter(id=request.user.id).exists():
        fav = True

    context = {
        'product': product,
        'products': products,
        'fav': fav,
    }
    return render(request, 'details.html', context)


def sotibqiz(request):
    return render(request, 'sotibqiz.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)


@ login_required
def favourite(request, id):
    post = get_object_or_404(Product, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
