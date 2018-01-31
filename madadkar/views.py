from django.shortcuts import render

def madadkarhome(request):
    return render(request,"home.html")

def madadkargoal(request):
    return render(request,"madadju-goals.html")

def madadkarhistory(request):
    return render(request,"madadju-history.html")

def madadkarchart(request):
    return render(request,"madadju-chart.html")

def madadkarcontact(request):
    return render(request,"madadju-contact.html")

def madadkarprofile(request):
    return render(request,"profile.html")

def editmadadju(request):
    return render(request,"edit-madadju.html")

def editneed(request):
    return render(request,"editneed.html")

def instantneed(request):
    return render(request,"instantneed.html")

def madadjuregister(request):
    return render(request,"madadju-register.html")

def managesaving(request):
    return render(request,"managesaving.html")

def receipt(request):
    return render(request,"receipt.html")

def report(request):
    return render(request,"report.html")

def seemsg(request):
    return render(request,"seemsg.html")

def seereq(request):
    return render(request,"seerequests.html")

def success(request):
    return render(request,"success.html")

def taaligh(request):
    return render(request,"taaligh.html")
