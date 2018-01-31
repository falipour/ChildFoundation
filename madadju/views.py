from django.shortcuts import render

def madadjuhome(request):
    return render(request, 'madadju.html')

def madadjugoal(request):
    return render(request, 'madadju-goals.html')

def madadjuhistory(request):
    return render(request, "madadju-history.html")

def madadjuchart(request):
    return render(request, "madadju-chart.html")

def madadjucontact(request):
    return render(request, "madadju-contact.html")

def madadkarchange(request):
    return render(request, "madadkarchange.html")

def madadjuprofile(request):
    return render(request, "profile.html")

def madadjumsg(request):
    return render(request, "sendmsg.html")

def madadjureq(request):
    return render(request, "sendreq.html")
