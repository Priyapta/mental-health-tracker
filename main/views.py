from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306245106',
        'name': 'Priyapta Naufal',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)

# Create your views here.
