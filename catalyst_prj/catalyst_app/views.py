from django.shortcuts import render
from django.shortcuts import render,redirect
from allauth.account.views import LoginView,SignupView,LogoutView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FileSerializer
import csv


def load_data(file_path):
    data = csv.reader(file_path, delimiter=',')
    csv_file = [list(row) for row in data]

    Created_data = []
    for i in csv_file:
        if len(i) >= 7:
            csv_data = Data(
                emp_id=i[0],
                name=i[1],
                domain=i[2],
                year=i[3],
                industry=i[4],
                size=i[5],
                area=i[6],
            )
            Created_data.append(csv_data) 
    Data.objects.bulk_create(Created_data)
        
@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['file']
            obj = File.objects.create(file=files)
            load_data(obj.file.path)
            return redirect('filter')
    else:
        form = UploadForm

    context = {'form': form}
    return render(request, 'upload.html', context)

@login_required
def filterdata_view(request):
    if request.method == 'GET':
        emp_id = request.GET.get('emp_id')
        name = request.GET.get('name')
        year = request.GET.get('year')
        domain = request.GET.get('domain')
        industry = request.GET.get('industry')
        size = request.GET.get('size')
        area = request.GET.get('area')

        filter_data = Data.objects.all()

        if emp_id:
            filter_data = filter_data.filter(Emp_id=emp_id)
        if name:
            filter_data = filter_data.filter(name=name)
        if year:
            filter_data = filter_data.filter(year=year)
        if domain:
            filter_data = filter_data.filter(domain=domain)
        if industry:
            filter_data = filter_data.filter(industry=industry)
        if size:
            filter_data = filter_data.filter(size=size)
        if area:
            filter_data = filter_data.filter(area=area)

        context = {
            'filtered_data': filter_data,
        }

        return render(request, 'filter.html', context)
    return render(request, 'filter.html')

@login_required
@api_view(['GET'])
def filterdata_api(request):
    emp_id = request.GET.get('emp_id')
    name = request.GET.get('name')
    year = request.GET.get('year')
    domain = request.GET.get('domain')
    industry = request.GET.get('industry')
    size = request.GET.get('size')
    area = request.GET.get('area')

    filter_data = Data.objects.all()

    if emp_id:
        filter_data = filter_data.filter(Emp_id=emp_id)
    if name:
        filter_data = filter_data.filter(name=name)
    if year:
        filter_data = filter_data.filter(year=year)
    if domain:
        filter_data = filter_data.filter(domain=domain)
    if industry:
        filter_data = filter_data.filter(industry=industry)
    if size:
        filter_data = filter_data.filter(size=size)
    if area:
        filter_data = filter_data.filter(area=area)

    serializer = FileSerializer(filter_data, many=True)
    return Response(serializer.data)


class CustomLoginView(LoginView):
    template_name = 'login.html'  
    
class CustomSignupView(SignupView):
    template_name = 'signup.html'
    
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'