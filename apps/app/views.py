# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

#from django.views.generic.edit import CreateView
import contextlib
from datetime import timezone
from datetime import datetime
from django.contrib.postgres import search
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Value
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template.loader import render_to_string
from django.template import loader
from django.urls import reverse, reverse_lazy
#from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView,  DetailView, DeleteView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.utils.html import format_html
from django.db.models import Q
from dal import autocomplete
from .forms import ConsumerForm

#from .backend.models_jugu import *
from .models import Consumer, Package, Package_Type,  Provider
from apps.app import forms

#from apps.app.middleware.global_request_middleare import GlobalRequestMiddleware
search_vector_jugu = SearchVector('last_name', weight='C') + SearchVector('first_name', weight='C')


def verified(view):
    def _decorated(request, *args, **kwargs):
        if not request.user.user_profile.is_verified:
            return HttpResponseRedirect(reverse_lazy('account:locked'))
        return view(request, *args, **kwargs)
    return _decorated

class ConsumerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Consumer.objects.none()

        qs = Consumer.objects.filter(is_responsable=True).all()

        if self.q :
            search = SearchQuery(self.q)
            qs = Consumer.objects.select_related().annotate(
                    rank=SearchRank(
                        search_vector_jugu,
                        search,
                        normalization=Value(2).bitor(Value(4)),
                    )
            ).filter(is_responsable=True,).order_by('-provided_at')


        return qs

    # def get_result_label(self, result):
    #     return format_html('<img src="flags/{}.png"> {}', result.name, result.name)


class GeneralSearchAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return ['Authentification Required!', ]#Consumer.objects.none()

        qs = Consumer.objects.select_related().filter().all()

        if self.q:
            qs = Consumer.objects.select_related().filter(name__istartswith=self.q).order_by('-provided_at')
        return qs

    # def get_result_label(self, result):
    #     return format_html('<img src="flags/{}.png"> {}', result.name, result.name)


class Index_View(TemplateView):
    #A mixin that can be used to render a template.
    template_name = 'index.html'
    #form_class = FormExample
    def get(self, request):
        context = {'segment': 'home'}
        return render(request, self.template_name, context=context)


decorators = [login_required(login_url='/login/'), verified]
@method_decorator(decorators, name='dispatch')
class Consumer_ListView( ListView):
    #template_name_suffix = '_list'
    """A mixin for views manipulating multiple objects."""
    #allow_empty = True
    #queryset = None
    model = Consumer
    paginate_by =  10
    #paginate_orphans = 0
    #context_object_name = None
    #paginator_class = Paginator
    #page_kwarg = 'page'
    #ordering = None
    context_object_name = 'data_jugu'
    # .order_by('-provided_at')
    queryset = Consumer.objects.select_related().filter(is_responsable=True).order_by('-provided_at').all()
    template_name = 'app/templates/consumer_list.html'

    def get_context_data(self, **kwargs):
        rr= super().get_context_data(**kwargs)
        rr['segment']='consumer_list'
        return rr

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            is_success = 0
            consumer = None
            provide_id = request.POST.get('id')
            if(provide_id and str(provide_id).isdigit()):
                provide_id = int(provide_id)
                consumer = self.model.objects.get(pk=provide_id)
                if(consumer):
                    consumer.provided_at = datetime.now()
                    consumer.num_packages = int(consumer.num_packages)+1
                    consumer.save(update_fields=["provided_at", "num_packages"])
                    is_success = 1
            return HttpResponse(f'The package N° {consumer.num_packages} is successfully provided for {consumer.first_name} {consumer.last_name} !')

    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.paginate_by = int(request.GET.get('paginate_by', 10)) or 10
        q = request.GET.get('q')
        responsable = request.GET.get('responsable')
        filter_jugu = request.GET.get('filter')
        if q:
            is_resp = True
            if(filter_jugu):
                mapper = {'-1':None, '1':True, '2':False}
                if(str(filter_jugu) in mapper):
                    is_resp = mapper[str(filter_jugu)]
                    print('is resp  = '+str(is_resp))

            self.queryset = Consumer.objects.select_related().filter(
                Q(last_name__icontains=q) | Q(first_name__icontains=q), is_responsable=is_resp).order_by('-provided_at')[:self.paginate_by]
            if request.is_ajax():
                if q == '___':
                    self.queryset = Consumer.objects.select_related().order_by('-provided_at').all()[:self.paginate_by]
                    
                html = render_to_string(            
                    template_name="includes/consumer_list_content.html",
                    context={"data_jugu": self.queryset}
                )
                #self.queryset=self.queryset.filter(is_responsable=is_resp)[:self.paginate_by]
                return HttpResponse(html)
        elif responsable:


            responsable = int(responsable)
            r = Consumer.objects.get(pk=responsable)
            if(not r.is_responsable):
                responsable = r.family_id if r.family_id else 0

            self.queryset = Consumer.objects.select_related().filter(
                Q(pk=responsable) | Q(family=responsable)).order_by('-is_responsable')[:self.paginate_by]

        return super().get(request,  * args, kwargs={'paginate_by':self.paginate_by })

    # def get_queryset(self):


    #     query = self.request.GET.get('q')  
    #     if query:
    #         object_list = self.model.objects.select_related().filter(last_name__icontains=query)
    #     else:
    #         object_list = self.model.objects.select_related().all()
    #     return object_list

@method_decorator(verified, name='dispatch')
class ConsumerCreateView( LoginRequiredMixin, CreateView):
    template_name = 'app/templates/consumer_form.html'
    form_class = ConsumerForm 
    queryset = Consumer.objects.prefetch_related()
    
    # def get_success_url(self):
    #     return reverse('profiles:detail', kwargs={'slug': self.slug})

    # def form_valid(self, form):
    #     profile = form.save(commit=False)
    #     image = form.cleaned_data['image']
    #     obj.user = self.request.user
    #     profile.save()


    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(user_jugu=request.user)
            return HttpResponseRedirect(reverse_lazy('app:consumer_list'))
        else:
            return render(request, self.template_name, {'form': form})


@method_decorator(verified, name='dispatch')
class ConsumerUpdateView(LoginRequiredMixin, UpdateView):
    #model = Consumer
    form_class = ConsumerForm
    template_name = 'app/templates/consumer_form.html'
    queryset = Consumer.objects.prefetch_related()
    #context_object_name = 'fd'
    #form_class = ConsumerForm
    success_url = reverse_lazy('app:consumer_list')


@method_decorator(verified, name='dispatch')
class ConsumerDeleteView(LoginRequiredMixin, DeleteView):
    model = Consumer
    success_url = reverse_lazy('app:consumer_list')
    template_name = 'app/templates/consumer_delete.html'

@login_required(login_url="/login/")
def consumers(request):
    context=[]
    context['data_jugu'] = Consumer.objects.all()# Context_jugu(page_name='consumers').get_context()
    return render(request, 'consumers.html', context=context)

@login_required(login_url="/login/")
@verified
def dashboard(request):
    context = {'segment': 'dashboard'}
    return render(request, 'dashboard.html', context=context)



@login_required(login_url="/login/")
def consumer_form(request, pk, action=''):
    context = {}
    dd = get_object_or_404(Consumer, pk=pk)
    errors = {}
    if request.method == "GET":
        if action == 'edit':
            print(f'[!] Action : {action} ({pk})')
            form = ConsumerForm(instance=dd, auto_id='%s', label_suffix=' : ')
            context = {'fd': form, }
            
            #print(form)
        elif action == 'delete':
            print(f'delete for! : {pk}')
        elif action == 'new':
            form = ConsumerForm()
            context = {'fd': form, }
        else:
            consumer_data = get_object_or_404(Consumer, pk=pk)
            form = ConsumerForm(consumer_data)
            context = {'fd': form, }
        #in all cases
        return render(request, 'app/templates/consumer_form.html', context=context)

    elif request.method == "POST":
        #print(request.POST)
        form = ConsumerForm(data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:consumer_form:', args=(pk,'edit',)))
            #assert False
        else:
            errors = form.errors
            print(errors)
            #form=ConsumerForm(data=request.POST)
            return render(request, 'app/templates/consumer_list.html',)
    else:
        form = ConsumerForm(request.POST)    
        print(request.POST)
        context = {'fd': form, }
    return render(request, 'app/templates/consumer_form.html', context=context)

'''

@login_required(login_url="/login/")
def pages(request):
    context = {}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template in ['admin']:
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        #return HttpResponse('Access forbidden by jugu!')
        #return render(request, 'dashboard.html', context=context)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print('-'*130)
        print(e)
        print('-'*130)
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
'''

