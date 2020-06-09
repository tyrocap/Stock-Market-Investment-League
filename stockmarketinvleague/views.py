import requests
import json
from .models import Company, Profile
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic.list import ListView
from stockmarketinvestmentleague.settings import IEXCLOUD_API
from django.core.exceptions import ObjectDoesNotExist


class homeView(ListView):
  model = Company
  paginate_by = 7
  template_name = 'home.html'


def search(request):
  if request.method == 'GET':
    ticker = request.GET['search_text'].upper()
    modal_companies = Company.objects.filter(
      symbol__contains=ticker)
    return JsonResponse(list(modal_companies.values()), safe=False)


def addwatchlist(request):
  try:
    # Get the profile connected to the user
    # Append the ticker to the waitlist array
    profile = Profile.objects.get(profile=request.user)
    profile.waitlist.append(request.POST['comp_symbol'])
    profile.save()
  except ObjectDoesNotExist:
    # If profile object doesnt exist yet,
    # create one with new ticker added to the waitlist
    profile = Profile.objects.create(profile=request.user, waitlist=[
      request.POST['comp_symbol'], ])
    profile.save()
  print(request.POST['comp_symbol'])
  print("The profile is successfully updated!")
  return redirect('home_view')


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
