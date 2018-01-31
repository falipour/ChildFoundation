from django.shortcuts import render

def madadjuhome(request):
    return render(request, 'madadju/madadju.html')

def madadjugoal(request):
    return render(request, 'madadju/madadju-goals.html')

def madadjuhistory(request):
    return render(request, "madadju/madadju-history.html")

def madadjuchart(request):
    return render(request, "madadju/madadju-chart.html")

def madadjucontact(request):
    return render(request, "madadju/madadju-contact.html")

def madadkarchange(request):
    return render(request, "madadju/madadkarchange.html")

def madadjuprofile(request):
    return render(request, "madadju/profile.html")

def madadjumsg(request):
    return render(request, "madadju/sendmsg.html")

def madadjureq(request):
    return render(request, "madadju/sendreq.html")
