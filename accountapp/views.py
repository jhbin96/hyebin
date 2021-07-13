from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        model_instance = NewModel() #import
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world')) #reverse alt+enter해서 import-장고

    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                        context = {'data_list': data_list})

