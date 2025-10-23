from django.shortcuts import render

def curriculo_spiff(request):
    return render(request, 'curriculo/curriculo-v1.html')

def curriculo_spiff_v2(request):
    return render(request, 'curriculo/curriculo-v2.html')