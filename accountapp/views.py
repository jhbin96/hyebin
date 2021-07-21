from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel

@login_required    #@login_required를 import
def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('input_text')

        model_instance = NewModel()  # import
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # reverse alt+enter해서 import-장고

    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                        context={'data_list': data_list})



class AccountCreateView(CreateView):  # import(alt+enter)
    model = User  # import
    form_class = UserCreationForm  # import
    success_url = reverse_lazy('accountapp:hello_world')  # reverse_lazy import
    template_name = 'accountapp/create.html'                #회원가입 로직완성


class AccountDetailView(DetailView): #import
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(login_required, 'get')    #import
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):          # 로직만들기, import하기
    model = User
    form_class = AccountCreationForm    #import
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(login_required, 'get')    #import
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView): #import
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
