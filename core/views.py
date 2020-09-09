from django.shortcuts import render

# Create your views here.

def pesquisa_servicos(request):
	return render(request, 'pesquisa_servicos.html')