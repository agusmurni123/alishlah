from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import User
from .models import DataBlog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user dibuat'
            return redirect('artikel:index')
        else:
            msg = 'form tidak valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form,'msg':msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('artikel:adminpage')
            elif user is not None and user.is_staff:
                login(request,user)
                return redirect('artikel:staff')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html',{'form':form,'msg':msg})


def admin(request):
    data_blogs = DataBlog.objects.all()
    return render(request, 'account/admin.html', {'object_list':data_blogs})

def staff(request):
    data_blogs = DataBlog.objects.all()
    return render(request, 'account/staff.html', {'object_list':data_blogs})

#view untuk konten

class IndexBlog(ListView):
    queryset = DataBlog.objects.all()

class TambahBlog(LoginRequiredMixin,CreateView):
    model = DataBlog
    fields =('judul', 'gambar', 'teks')
    success_url = reverse_lazy('artikel:konten')

    def form_valid(self, form):
        form.instance.penulis = self.request.user
        return super().form_valid(form)

class DetailBlog(DetailView):
    model = DataBlog

class HapusBlog(DeleteView):
    model = DataBlog
    fields = '__all__'
    success_url = reverse_lazy('artikel:konten')

class UbahBlog(UpdateView):
    model = DataBlog
    fields = '__all__'
    success_url = reverse_lazy('artikel:konten')

# multi konten staff
@login_required(login_url='/login/')  # Pastikan hanya pengguna yang login yang dapat mengakses halaman staff
def staff(request):
    # Ambil semua data blog yang dibuat oleh pengguna saat ini
    data_blogs = DataBlog.objects.filter(penulis=request.user)
    return render(request, 'account/staff.html', {'object_list': data_blogs})