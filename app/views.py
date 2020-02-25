from django.shortcuts import render, redirect


def index(request):
    return render(request, 'app/index.html', context=None)

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def MVP_treasure_hunt(request):
	return render(request, 'MVP_treasure_hunt.html')
