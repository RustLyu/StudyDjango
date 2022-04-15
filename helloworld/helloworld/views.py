
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
def hello(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')
    else:
        return HttpResponse("Hello world ! ")
    

def runoob(request):
    context = {}
    context['hello'] = 'Hello world!'
    return render(request, 'runoob.html', context)
