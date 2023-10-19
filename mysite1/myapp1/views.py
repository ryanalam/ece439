from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return render(request, 'fibonacci.html')

def calculate_fibonacci(request):
    if request.method == 'POST':
        try:
            number = int(request.POST.get('number'))
            fibonacci_result = calculate_fib(number)
            return render(request, 'fibonacci.html', {'number': number, 'fibonacci_result': fibonacci_result})
        except ValueError:
            error_message = "Please enter a valid number."
            return render(request, 'fibonacci.html', {'error_message': error_message})
    else:
        return HttpResponse("Invalid request method")

def calculate_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fib(n - 1) + calculate_fib(n - 2)
    
def create(request):
    data = Student.objects.all()  # Define data outside of if-else block
    
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            student_id = fm.cleaned_data['id']
            if Student.objects.filter(id=student_id).exists():
                messages.error(request, 'ID already taken! Use another ID')
            else:
                fm.save()
                return redirect('crud')
        else:
            # Form is not valid, display error messages
            for field, errors in fm.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        fm = StudentForm()

    
    return render(request, 'crud.html', {'fm': fm, 'data': data})


def edit(request,id):
    dataget = Student.objects.get(id=id)
    data = Student.objects.all()
    fm = StudentForm(instance=dataget)
    if request.method == 'POST':
        fm = StudentForm(request.POST,instance=dataget)
        if fm.is_valid():
            fm.save()
            return redirect('crud')
    return render(request,'crud.html',{'fm':fm,'data':data})

def delete(request,id):
    dataget = Student.objects.get(id=id)
    dataget.delete()
    return redirect('crud')
