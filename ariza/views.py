from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Application, Direction
from .forms import ApplicationForm, AdminCreateForm
from xhtml2pdf import pisa
from django.template.loader import get_template
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ariza/success.html')
    else:
        form = ApplicationForm()
    return render(request, 'ariza/application_form.html', {'form': form})


def application_pdf(request, pk):
    application = get_object_or_404(Application, pk=pk)
    template_path = 'ariza/application_pdf.html'
    context = {'application': application}
    response = HttpResponse(content_type='application/pdf')
    filename = f"{application.last_name}_{application.first_name}_ariza_{application.pk}.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF yaratishda xatolik yuz berdi')
    return response

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error = 'Login yoki parol noto‘g‘ri!'
    return render(request, 'ariza/admin_login.html', {'error': error})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url='/admin-login/')
@user_passes_test(is_admin, login_url='/admin-login/')
def admin_dashboard(request):
    applications_count = Application.objects.count()
    admins_count = User.objects.filter(is_staff=True).count()
    accepted_count = Application.objects.filter(status='accepted').count()
    rejected_count = Application.objects.filter(status='rejected').count()
    pending_count = Application.objects.filter(status='pending').count()
    return render(request, 'ariza/admin_dashboard.html', {
        'applications_count': applications_count,
        'admins_count': admins_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count,
        'pending_count': pending_count,
    })

@login_required(login_url='/admin-login/')
@user_passes_test(is_admin, login_url='/admin-login/')
def admin_applications(request):
    applications = Application.objects.all().order_by('-created_at')
    return render(request, 'ariza/admin_applications.html', {'applications': applications})

@login_required(login_url='/admin-login/')
@user_passes_test(is_admin, login_url='/admin-login/')
def admin_application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        if 'set_status' in request.POST:
            new_status = request.POST.get('set_status')
            if new_status in dict(Application.STATUS_CHOICES):
                application.status = new_status
                application.save()
                return redirect('admin_application_detail', pk=pk)
        if 'delete_passport' in request.POST:
            if application.passport_image:
                application.passport_image.delete(save=False)
                application.passport_image = None
                application.save()
            return redirect('admin_application_detail', pk=pk)
        if 'delete_selfie' in request.POST:
            if application.selfie_image:
                application.selfie_image.delete(save=False)
                application.selfie_image = None
                application.save()
            return redirect('admin_application_detail', pk=pk)
    return render(request, 'ariza/admin_application_detail.html', {'application': application})

@login_required(login_url='/admin-login/')
@user_passes_test(is_admin, login_url='/admin-login/')
def admin_admins(request):
    admins = User.objects.filter(is_staff=True)
    return render(request, 'ariza/admin_admins.html', {'admins': admins})

@login_required(login_url='/admin-login/')
@user_passes_test(is_admin, login_url='/admin-login/')
def admin_add(request):
    if request.method == 'POST':
        form = AdminCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_admins')
    else:
        form = AdminCreateForm()
    return render(request, 'ariza/admin_add.html', {'form': form})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
