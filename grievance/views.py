from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from .models import Grievance
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from datetime import datetime, timedelta
import dateutil
import pytz




def home(request):
    #grievances= Grievance.objects.values('grev_id')
    return render(request, 'grievance/home.html')

@login_required(login_url="/accounts/signup")
def log(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['content'] and request.POST['name'] and request.POST['phone_number'] and request.POST['position'] and request.POST['gender']:
            grievance = Grievance()
            grievance.title = request.POST['title']
            grievance.body = request.POST['content']
            grievance.Name = request.POST['name']
            grievance.re_date = timezone.datetime.now()
            grievance.grev_id = request.user
            grievance.user = request.user.username
            grievance.phone_number = request.POST['phone_number']
            grievance.position = request.POST['position']
            grievance.gender = request.POST['gender']
            grievance.save()
            return render(request, 'grievance/log_complain.html',{'error':'You Have Successfully file a grievance'})
        else:
            return render(request, 'grievance/log_complain.html',{'error':'All Field Are Required'})
    else:
        return render(request, 'grievance/log_complain.html')



@staff_member_required(login_url="/accounts/signup")
def  view(request):
    grievances= Grievance.objects.filter(status= 0 ).order_by('-re_date')

    # grievance =  list(Grievance.objects.all().values())
    # grievance =serialize('json', Grievance.objects.filter(status= 0))
    # data =  dict()
    # data['grievance'] = grievance
#    return JsonResponse(data)

    return render(request, 'grievance/view.html',{'grievances': grievances})


@user_passes_test(lambda u: u.is_superuser)
def  resolve(request):
    grievances= Grievance.objects.filter(status= 2).order_by('-re_date')
    return render(request, 'grievance/resolve.html',{'grievances': grievances})


        # grievance =  list(Grievance.objects.all().values())
        # grievance =serialize('json', Grievance.objects.filter(status= 0))
        # data =  dict()
        # data['grievance'] = grievance
    #    return JsonResponse(data)



@staff_member_required(login_url="/accounts/signup")
def approve(request, grievance_id):
    grievance = get_object_or_404(Grievance, pk=grievance_id)
    if request.method == 'POST':
            grievance.status = 2
            grievance.verified=request.user.username
            grievance.verifeedback = request.POST['verifeedback']
            grievance.v_date = timezone.datetime.now()
            grievance.type = request.POST['type']
            grievance.save()
            return render(request, 'grievance/home.html',{'error':'You Have Successfully verify'})
    else:
        return render(request, 'grievance/approve.html',{'grievance':grievance})

@staff_member_required(login_url="/accounts/signup")
def reject(request, grievance_id):
    grievance = get_object_or_404(Grievance, pk=grievance_id)
    if request.method == 'POST':
            grievance.status = 10
            grievance.verified=request.user.username
            grievance.v_date = timezone.datetime.now()
            grievance.verifeedback = request.POST['verifeedback']
            grievance.save()
            return render(request, 'grievance/home.html',{'error':'You Have Successfully Rejected The Complain'})
    else:
        return render(request, 'grievance/reject.html',{'grievance':grievance})

@user_passes_test(lambda u: u.is_superuser)
def resolvefeedback(request, grievance_id):
    grievance = get_object_or_404(Grievance, pk=grievance_id)
    if request.method == 'POST':
            grievance.status = 4
            grievance.r_date = timezone.datetime.now()
            grievance.resolvefeedback = request.POST['resolvefeedback']
            grievance.save()
            return render(request, 'grievance/home.html',{'error':'You Have Successfully Resolve'})
    else:
        return render(request, 'grievance/resolvefeedback.html',{'grievance':grievance})

def  viewstatus(request):
    name = request.user.username
    grievances= Grievance.objects.filter(user=name).order_by('-re_date')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    # print (grievances)
    return render(request, 'grievance/viewstatus.html',{'grievances':grievances})

def  status(request , grievance_id):
    grievance = get_object_or_404(Grievance, pk=grievance_id)
    # print (grievances)
    return render(request, 'grievance/status.html',{'grievance': grievance})

@user_passes_test(lambda u: u.is_superuser)
def  statistic(request):

    #grievances= Grievance.objects.filter(user=name).order_by('-re_date')
    #week = Grievance.objects.filter(re_date=(timezone.now() - datetime.timedelta(days=7)).count()
    grievances = Grievance.objects.count()
    reject = Grievance.objects.filter(status= 10).count()
    pending = Grievance.objects.filter(status= 2).count()
    resolve = Grievance.objects.filter(status= 4).count()
    male = Grievance.objects.filter(gender = 'M').count()
    female = Grievance.objects.filter(gender = 'F').count()
    # some_day_last_week = timezone.now().date() - timedelta(days=7)
    # now = datetime.datetime.now()
    # earlier = now - datetime.timedelta(hours=24)
    # results = Grievance.objects.filter(re_date=(earlier,now))
    # results=Grievance.filter(re_date=datetime.today())

    #today = Grievance.objects.filter(re_date = date.today()).count()
    #today = Grievance.objects.filter(re_date=datetime.now().strftime('%m-%d-%Y')).count()

    #week =Grievance.objects.filter(  re_date=52).count()
    # print(results)
    #week = Grievance.objects.filter(re_date=(timezone.now() - datetime.timedelta(days=7))
    return render(request, 'grievance/statistic.html',context={'grievances':grievances,'reject':reject,'pending':pending,'resolve':resolve,'male':male,'female':female})

    #current = timezone.now().date()
    #some_day_last_week = date.today() - timedelta(days=7)
    #some_day_last_week = dateutil.parser.parse(some_day_last_week).replace(tzinfo=pytz.UTC)



    #some_day_last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    #current = datetime.datetime.now()



    #grievance = get_object_or_404(Grievance, pk=grievance_id)

    #week = Grievance.objects.filter(re_date=[some_day_last_week , current]).count()



@user_passes_test(lambda u: u.is_superuser)
def  computerscience(request):
    grievances= Grievance.objects.filter(position = 'CS')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    #print (grievances)
    return render(request, 'grievance/computerscience.html',{'grievances':grievances})


@user_passes_test(lambda u: u.is_superuser)
def  mechanical(request):
    grievances= Grievance.objects.filter(position = 'M')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    #print (grievances)
    return render(request, 'grievance/mechanical.html',{'grievances':grievances})

@user_passes_test(lambda u: u.is_superuser)
def  etc(request):
    grievances= Grievance.objects.filter(position = 'E')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    #print (grievances)
    return render(request, 'grievance/etc.html',{'grievances':grievances})

@user_passes_test(lambda u: u.is_superuser)
def  civil(request):
    grievances= Grievance.objects.filter(position = 'C')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    #print (grievances)
    return render(request, 'grievance/civil.html',{'grievances':grievances})

@user_passes_test(lambda u: u.is_superuser)
def  electric(request):
    grievances= Grievance.objects.filter(position = 'EE')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    #print (grievances)
    return render(request, 'grievance/electric.html',{'grievances':grievances})

@user_passes_test(lambda u: u.is_superuser)
def  faculty(request):
    grievances= Grievance.objects.filter(position = 'F')
    #grievance = get_object_or_404(Grievance, pk=grievance_id)
    #print (grievances)
    return render(request, 'grievance/faculty.html',{'grievances':grievances})
