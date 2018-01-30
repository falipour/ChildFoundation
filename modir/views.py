from django.views.generic import TemplateView


class AdminGoalsView(TemplateView):
    template_name = 'modir/Admin_Goals.html'


class AdminHomeView(TemplateView):
    template_name = 'modir/Admin_Home.html'


class AdminContactView(TemplateView):
    template_name = 'modir/Admin_Contact.html'


class AdminHistoryView(TemplateView):
    template_name = 'modir/Admin_History.html'


class AdminChartView(TemplateView):
    template_name = 'modir/Admin_Chart.html'
