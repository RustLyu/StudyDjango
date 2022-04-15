from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    valid_num = request.POST.get("valid_num")
    keep_str = request.session.get("keep_str")
    if True:
    # if keep_str.upper() == valid_num.upper():
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj.username)
        if not user_obj:
            return redirect("/login/")
        else:

            auth.login(request, user_obj)
            path = request.GET.get("next") or "/index/"
            print(path)
            rep = redirect(path)
            rep.set_cookie("is_login", True)
            return rep
    else:
        return redirect("/login/")

def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
    