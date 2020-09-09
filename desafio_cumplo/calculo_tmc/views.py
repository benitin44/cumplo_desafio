from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from .forms import CalculadoraForm
from .services.sbif.api import getTasaMaximaConvencional
# Create your views here.




def index(request):
    return render(request, 'calculadora/calculadora.html')

def get_tmc(request):
    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
    else:
        return HttpResponse("Method not allowed.")
    
    if form.is_valid():
#        return render(request , 'result.html', {'form': form})
        tmc = getTasaMaximaConvencional(form.cleaned_data['fecha'],form.cleaned_data['monto'], form.cleaned_data['plazo'],form.cleaned_data['is_reajustable'], form.cleaned_data['is_extranjera'])
        print(tmc)
        print(form.cleaned_data)
        return render(request , 'calculadora/calculadora.html', {'result':tmc , 'form':form.cleaned_data })
    else:
        return HttpResponse("Invalid data , try again.")