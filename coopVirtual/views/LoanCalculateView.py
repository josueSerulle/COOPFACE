from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coopVirtual.backends.LoandApplicationBackEnd import LoandApplicationBackEnd
from coopVirtual.backends.LoanCalculateBackEnd import LoanCalculateBackEnd
from ..decorators import partner_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='login_coop')
@partner_required
def indexView(request):
    LoanApplication = LoandApplicationBackEnd()
    return render(request, "coopVirtual/loanCalculate/index.html", {"loandTypes": LoanApplication.getAllLoandType()})

@login_required(login_url='login_coop')
def loandCalculateView(request):
    
    if request.method == "GET":
        interes     = float(request.GET['interes'])
        amount      = float(request.GET['amount'].replace("$","").replace(",",""))
        cuotes      = int(request.GET['cuotes'])

        loanCalculate = LoanCalculateBackEnd()

        return JsonResponse({"data": loanCalculate.calculate(interes, amount, cuotes)}, safe = False)