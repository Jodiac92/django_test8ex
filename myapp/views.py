from django.shortcuts import render, render_to_response
from myapp.models import Buser, Jikwon, Gogek

# Create your views here.

def MainFunc(request):
    datas1 = Buser.objects.all()
    return render(request, 'main.html', {'buser':datas1})

def JikwonFunc(request):
    jikname = request.GET['buser_no']
    jikDatas = Jikwon.objects.all().filter(buser_num=jikname)
    return render(request, 'jikwon.html', {'jikwon':jikDatas})

def GogekFunc(request):
    jikwon_no = request.GET['jikwon']
    gogekDatas = Gogek.objects.all().filter(gogek_damsano=jikwon_no)
    return render(request, 'gogek.html', {'gogek':gogekDatas})
    
    
# def jikwonFunc(request):
#     jikDatas = Jikwon.objects.get(buser_name=request.POST.get('buser_name'))
#     return render(request, 'jikwon.html', {'jikwon':jikDatas})