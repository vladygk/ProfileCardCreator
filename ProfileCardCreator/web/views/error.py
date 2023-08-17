from django.shortcuts import render
from django.views import View
from django.template.loader import get_template
from django.http import HttpResponseServerError
from django.views.generic import TemplateView


class Custom403View(View):
    def get(self, request, *args, **kwargs):
        template = get_template('error/403.html')
        return HttpResponseServerError(template.render({'error_code': 403}, request))


class Custom404View(TemplateView):
    template_name = 'error/404.html'
