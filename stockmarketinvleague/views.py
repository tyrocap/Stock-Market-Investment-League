import requests
import json
from .models import Company
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from stockmarketinvestmentleague.settings import IEXCLOUD_API


class homeView(ListView):
  model = Company
  paginate_by = 8
  template_name = 'home.html'


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
      comp.marketCap = obj['marketCap']//1000000
      comp.ytdChange = round(obj['ytdChange'], 2)
      comp.save()

    return redirect('home_view')

  # quote = {
  #   'symbol': 'JPM',
  #   'companyName': 'JPMorgan Chase & Co.',
  #   'primaryExchange': 'New York Stock Exchange',
  #   'calculationPrice': 'iexlasttrade',
  #   'open': None,
  #   'openTime': None,
  #   'openSource': 'official',
  #   'close': None,
  #   'closeTime': None,
  #   'closeSource': 'official',
  #   'high': None,
  #   'highTime': 1590695995868,
  #   'highSource': '15 minute delayed price',
  #   'low': None,
  #   'lowTime': 1590678352186,
  #   'lowSource': '15 minute delayed price',
  #   'latestPrice': 99.84,
  #   'latestSource': 'IEX Last Trade',
  #   'latestTime': 'May 28, 2020',
  #   'latestUpdate': 1590695994739,
  #   'latestVolume': None,
  #   'iexRealtimePrice': 99.84,
  #   'iexRealtimeSize': 5,
  #   'iexLastUpdated': 1590695994739,
  #   'delayedPrice': None,
  #   'delayedPriceTime': None,
  #   'oddLotDelayedPrice': None,
  #   'oddLotDelayedPriceTime': None,
  #   'extendedPrice': None,
  #   'extendedChange': None,
  #   'extendedChangePercent': None,
  #   'extendedPriceTime': None,
  #   'previousClose': 101.37,
  #   'previousVolume': 39402040,
  #   'change': -1.53,
  #   'changePercent': -0.01509,
  #   'volume': None,
  #   'iexMarketPercent': 0.015464972162976862,
  #   'iexVolume': 380049,
  #   'avgTotalVolume': 23932798,
  #   'iexBidPrice': 0,
  #   'iexBidSize': 0,
  #   'iexAskPrice': 0,
  #   'iexAskSize': 0,
  #   'iexOpen': None,
  #   'iexOpenTime': None,
  #   'iexClose': 99.84,
  #   'iexCloseTime': 1590695994739,
  #   'marketCap': 304214476800,
  #   'peRatio': 11.24,
  #   'week52High': 141.1,
  #   'week52Low': 76.91,
  #   'ytdChange': -0.296612,
  #   'lastTradeTime': 1590695994739,
  #   'isUSMarketOpen': False}
