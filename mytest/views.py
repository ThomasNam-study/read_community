from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mytest(request):

    print("GET")
    for k, v in request.GET.items():
        print(k + " = " + v)

    print("POST")
    for k, v in request.POST.items():
        print(k + " = " + v)

    return render(request, 'index.html', {})
