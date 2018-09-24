from django.shortcuts import render, render_to_response
from Accounts.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader, Context
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.core.urlresolvers import reverse
import pyrebase
# Create your views here.

config = {
    'apiKey': "AIzaSyC4Xco0toRujN2iwd76dcUAREm7A5eRnl8",
    'authDomain': "myspecialist-586a1.firebaseapp.com",
    'databaseURL': "https://myspecialist-586a1.firebaseio.com",
    'projectId': "myspecialist-586a1",
    'storageBucket': "myspecialist-586a1.appspot.com",
    'messagingSenderId': "970425742425"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

'''def stream_handler(message):
    print("Hello")
    print(my_stream)
    return HttpResponse("<script>notify.hello();</script>")
    #return HttpResponseRedirect('/patients/')
my_stream = database.child("users").stream(stream_handler)
print(my_stream)'''

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    print("Hello")
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        #user = authenticate(email=email, password=password)
        user = auth.sign_in_with_email_and_password(email,password)
        #session_id=user['idToken']
        #request.session['uid'] = str(session_id)
        return HttpResponseRedirect('/dashboard/')
    d = dict(form.errors)
    return render(request, 'log_in.html', {"form":form, "errors":d})

def patients_view(request):
    #idtoken = request.session['uid']
    #a = auth.get_account_info(idtoken)
    #print("Printing a")
    #print(a)
    print("Inside patients view")
    l = []
    all_users = database.child('users').get()
    for user in all_users.each():
        t = user.val()
        t.update({"uid":user.key()})
        l.append(t)
    #l = []
    #for obj in users_l:
    #    l.append(obj)
    #print(l)
    #name = database.child('users').child(l[0])
    #print(name)
    return render(request, 'table.html', {"form": l})

def dashboard_view(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def profile_view(request):
    #msg = request.POST.get('msgbox')
    #request.method = 'POST'
    print("Oye hoye")
    #msg = request.POST.get['uid']
    #print(msg)
    #user = database.child('users').child(msg).get().val()
    #return JsonResponse({ 'msg': msg })
    uid = "j8LPz3YGRsZj2iLvRAUfpDlmnOr1"
    user = database.child('users').child(uid).get().val()
    images = user["Images"].values()
    #return JsonResponse({ 'msg': msg })
    print("Idhar pohchah")
    print("Kya haal hai")
    #return HttpResponseRedirect(reverse('/patients/profile', kwargs = {"form": user, "images": images}))
    #return HttpResponse('profile')
    #return render_to_response('profile.html', { "form": user, "images": images },  RequestContext(request))
    #return redirect('profi le.html', {"form": user, "images": images})
    return render(request , 'profile.html', {"form": user, "images": images})

@csrf_exempt
def verify_view(request):
    print("Inside verify")
    form = OtpForm()
    if request.method == 'POST':
        form = OtpForm(request.POST)
        print(form)
        cd = form.cleaned_data
        otp = cd['otp']
        uid = "j8LPz3YGRsZj2iLvRAUfpDlmnOr1"
        user = database.child('users').child(uid).get().val()
        print(user["OTP"])
        print(otp)
        if int(otp) == int(user["OTP"]):
            data = {"flag": 1,}
            database.child("users").child(uid).update(data)
            return HttpResponseRedirect('/profile/')
    return render(request , 'otp.html', {'form': form})
