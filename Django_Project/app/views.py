from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    # return HttpResponse('hello')
    title = '何哲平的Flask'
    return render(request,'app\hello.html', {'title':title})

def frontpage(request):
    return render(request,'app\index.html', {})
