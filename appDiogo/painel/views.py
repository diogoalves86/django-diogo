# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
	nome = 'Diogo'
	numeros = [1,2,3.4]
	args = {'nome': nome, 'numeros':numeros}
	return render(request, 'painel/login.html', args)
