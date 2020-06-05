import requests
import json
from .models import Company
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic.list import ListView
from stockmarketinvestmentleague.settings import IEXCLOUD_API


class homeView(ListView):
  model = Company
  paginate_by = 7
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if self.request.GET:
      ticker = self.request.GET['search_text'].upper()
      context['modal_companies'] = Company.objects.filter(
        symbol__contains=ticker)
      return context
    else:
      return context

def search(request):
  if request.method == 'GET':
    ticker = request.GET['search_text'].upper()
    modal_companies = Company.objects.filter(
      symbol__contains=ticker)
    print(list(modal_companies.values()))
    return JsonResponse(list(modal_companies.values()), safe=False)

def get_data(request):
  if request.method == 'GET':

    companies = Company.objects.all()
    for comp in companies:
      ticker = comp.symbol
      # make a request
      url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote'
      params = {
        "token": IEXCLOUD_API,
      }

      # get the data
      request = requests.get(url, params)
      obj = json.loads(request.text)

      comp.price = round(obj['latestPrice'], 2)
      comp.low_high = [obj['week52High'], obj['week52Low']]
      comp.marketCap = obj['marketCap'] // 1000000
      comp.ytdChange = round(obj['ytdChange'], 2)
      comp.save()

    return redirect('home_view')
