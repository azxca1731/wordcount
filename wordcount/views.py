from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    url = request.GET['fulltext']
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find('body').prettify()
    hangul = hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('',body)

    words = result.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'result.html', {'dictionary': word_dictionary, 'url': url, 'total': len(result)})