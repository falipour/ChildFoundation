from django.shortcuts import render

def madadjuhome(request):
    render(request,"../templates/madadju/madadju.html")

def madadjugoal(request):
    render(request,"../templates/madadju/madadju-goals.html")

def madadjuhistory(request):
    render(request,"../templates/madadju/madadju-history.html")

def madadjuchart(request):
    render(request,"../templates/madadju/madadju-chart.html")

def madadjucontact(request):
    render(request,"../templates/madadju/madadju-contact.html")

def madadkarchange(request):
    render(request,"../templates/madadju/madadkarchange.html")

def madadjuprofile(request):
    render(request,"../templates/madadju/profile.html")

def madadjumsg(request):
    render(request,"../templates/madadju/sendmsg.html")

def madadjurequest(request):
    render(request,"../templates/madadju/sendreq.html")
