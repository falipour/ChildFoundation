from django.views.generic import TemplateView


class AdminGoalsView(TemplateView):
    template_name = 'modir/Admin_Goals.html'
