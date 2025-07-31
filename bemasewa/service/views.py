from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Service, Application
from .forms import ApplicationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import PanCardApplicationForm,LifeInsuranceForm
from .models import PanCardApplication, LifeInsuranceApplication
from django.contrib import messages



def homepage(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.service = service
            application.user = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'services/service_detail.html', {'service': service, 'form': form})

@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'services/dashboard.html', {'applications': applications})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'services/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'services/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')
@login_required
def apply_pan(request):
    if request.method == 'POST':
        form = PanCardApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()
            messages.success(request,"Your PAN registeraction is success!")
    else:
        form = PanCardApplicationForm()
    return render(request, 'services/apply_pan.html', {'form': form})

@login_required
def apply_insurance(request):
    if request.method == 'POST':
        form = LifeInsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Life Insurance registeraction is success!")

    else:
        form = LifeInsuranceForm()
    return render(request, 'services/apply_life.html', {'form': form})


def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# View to list PAN card applications
@login_required
@superuser_required
def list_pan_applications(request):
    applications = PanCardApplication.objects.all()
    return render(request, 'superuser/list_pan_applications.html', {'applications': applications})

# View to list Life Insurance applications
@login_required
@superuser_required
def list_life_insurance(request):
    applications = LifeInsuranceApplication.objects.all()
    return render(request, 'superuser/list_life_insurance.html', {'applications': applications})


@login_required
def my_pan_applications(request):
    my_apps = PanCardApplication.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'services/my_pan_status.html', {'applications': my_apps})

@login_required
def my_life_applications(request):
    my_apps = LifeInsuranceApplication.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'services/my_life_status.html', {'applications': my_apps})


@login_required
@superuser_required
def approve_pan(request, pk):
    app = get_object_or_404(PanCardApplication, pk=pk)
    app.status = 'Approved'
    app.rejection_note = ''
    app.save()
    messages.success(request, f"PAN application #{app.id} approved.")
    return redirect('list_pan')

@login_required
@superuser_required
def reject_pan(request, pk):
    if request.method == 'POST':
        app = get_object_or_404(PanCardApplication, pk=pk)
        note = request.POST.get('note', '')
        app.status = 'Rejected'
        app.rejection_note = note
        app.save()
        messages.warning(request, f"PAN application #{app.id} rejected.")
    return redirect('list_pan')
@login_required
@superuser_required
def approve_life(request, pk):
    app = get_object_or_404(LifeInsuranceApplication, pk=pk)
    app.status = 'Approved'
    app.rejection_note = ''
    app.save()
    messages.success(request, f"Life insurance application #{app.id} approved.")
    return redirect('list_life')

@login_required
@superuser_required
def reject_life(request, pk):
    if request.method == 'POST':
        app = get_object_or_404(LifeInsuranceApplication, pk=pk)
        note = request.POST.get('note', '')
        app.status = 'Rejected'
        app.rejection_note = note
        app.save()
        messages.warning(request, f"Life insurance application #{app.id} rejected.")
    return redirect('list_life')

