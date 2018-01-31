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
