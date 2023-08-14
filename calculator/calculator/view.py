from django.http import HttpResponse
from django.shortcuts import render

def calculator(request):
    c =''
    try:
        if request.method =='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            opr= request.POST.get('opr')
            if opr == "+":
                c = n1+n2
            elif opr =="-":
                c = n1-n1;    
            elif opr == "*":
                c = n1*n2;   
            elif opr =="/":
                c = n1/n2
    except:
        c ="invalid input....."    
    return render(request,"calculator.html",{'c':c})        