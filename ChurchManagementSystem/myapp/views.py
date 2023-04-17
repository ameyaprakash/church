from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import confession,marriage,baptism,prayerdetails,sermons,events,funddetails
from .form import staffForm,baptismForm,confessionForm,eventsForm,sermonsdetailsForm,marriagForm,prayerdetailsForm,funddetailsForm
# Create your views here.

def login(request):
    return render(request,"Admin/login.html")
def login_post(request):
    username=request.POST['usrname']
    password=request.POST['pswd']
    lobj=login.objects.filter(username=username,password=password)
    if lobj.exists():
        lobjj=login.objects.get(username=username,password=password)
        if lobjj.type=='admin':
            return redirect('/myapp/')
    return HttpResponse("ok")

def admin_home(request):
    return render(request,"Admin/admin home.html")

def admin_password(request):
    return render(request,"Admin/chngpswd.html")
def admin_view_complaint(request):
    return render(request,"Admin/ad reply.html")

def admin_add_staff(request):
    return render(request,"Admin/add staff.html")
def admin_staff_post(request):
    # staff_name=request.POST['name']
    # place=request.POST['place']
    # post=request.POST['post']
    # pin=request.POST['pin']
    # phone_no=request.POST['phone no']
    # email=request.POST['email']
    # photo=request.POST['image']
    # gender=request.POST['female']
    # gender1=request.POST['male']
    if request.method== "POST":
        form=staffForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":staffForm()})

def admin_donation(request):
    return render(request,"Admin/admin_donation.html")

def admin_complaint_reply(request):
    return render(request,"Admin/com reply.html")

def admin_add_committee(request):
    return render(request,"Admin/committee.html")
def admin_committee_post(request):
    committename=request.POST['name']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    phoneno=request.POST['phoneno']
    email=request.POST['email']
    photo=request.POST['photo']
    gender=request.POST['male']
    gender1=request.POST['female']
    gender2=request.POST['other']
    return HttpResponse("ok")



def admin_manage_commitee(request):
    return render(request,"Admin/m_comm.html")
def admin_manage_staff(request):
    return render(request,"Admin/m_staff.html")

def admin_report_view(request):
    return render(request,"Admin/rpt view.html")




def committee_add_event(request):
    if request.method== "POST":
        form=eventsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":eventsForm()})
def view_committee_event(request):
    context={"data":events.objects.all()}
    return render(request,"Committee/view_event.html",context)
def committe_event_post(request):
    eventname=request.POST['evtname']
    eventdetails=request.POST['evtdetails']
    evntdescptn=request.POST['descptn']
    date=request.POST['date']
    time=request.POST['time']
    place=request.POST['place2']
    return HttpResponse("ok")


def committee_add_fund(request):
    if request.method== "POST":
        form=funddetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":funddetailsForm()})
def committe_fund_post(request):
    funddetails=request.POST['fund']
    expenditure=request.POST['exp']
    date=request.POST['date']
    return HttpResponse("ok")

def view_funddetails(request):
    context={"data":funddetails.objects.all()}
    return render(request,"Committee/view_funds.html",context)

def committee_view_participants(request):
    return render(request,"Committee/event view.html")
def committee_manage_event(request):
    return render(request,"Committee/event.html")
def committee_event_report(request):
    return render(request,"Committee/report.html")

def staff_home(request):
    return render(request,"Staff/home.html")
def staff_add_sermons(request):
        if request.method== "POST":
            form=sermonsdetailsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("saved")
            else:
                return HttpResponse("invalid")
        else:
            return render(request,"form.html",{"form":sermonsdetailsForm()})

def view_sermons(request):
    context={"data":sermons.objects.all()}
    return render(request,"Staff/veiw_sermons.html",context)
    # return render(request,"Staff/add sermons.html")
def staff_sermons_post(request):
    sermondesc=request.POST('description')
    date=request.POST('date')
    time=request.POST('time')
    return HttpResponse("ok")


def staff_baptism(request):
    return render(request,"Staff/baptism.html")

def add_baptism(request):
    if request.method== "POST":
        form=baptismForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":baptismForm()})

def view_baptism(request):
    context={"data":baptism.objects.all()}
    return render(request,"Staff/view_baptism.html",context)
def staff_confession(request):
    return render(request,"Staff/confession.html")

def add_confession(request):
    if request.method== "POST":
        form=confessionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":confessionForm()})

def view_confession(request):
    context={"data":confession.objects.all()}
    return render(request,"Staff/veiw_confesssion.html",context)

def staff_marriage(request):
    return render(request,"Staff/marriage.html")
def add_marriage(request):
    if request.method== "POST":
        form=marriagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":marriagForm()})

def view_marriage(request):
    context={"data":marriage.objects.all()}
    return render(request,"Staff/view_marriage.html",context)
def staff_prayer(request):
    return render(request,"Staff/prayer rqst.html")
def add_prayer(request):
    if request.method== "POST":
        form=prayerdetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"form.html",{"form":prayerdetailsForm()})

def view_prayer(request):
    context={"data":prayerdetails.objects.all()}
    return render(request,"Staff/veiw_prayer.html",context)

def user_confession(request):
    return render(request,"User/confession rqst.html")
def user_marriage(request):
    return render(request,"User/marriage rqst.html")
def user_prayer(request):
    return render(request,"User/prayer.html")
def user_donation(request):
    return render(request,"User/donation.html")
def user_donation_post(request):
    donationtype=request.POST('')
    description=request.POST('')
    date=request.POST('')
    return HttpResponse("ok")





