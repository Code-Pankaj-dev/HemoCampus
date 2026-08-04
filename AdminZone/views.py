from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password
from AdminZone.models import LoginModel
def dashboard(request):
    if request.session.has_key('aid'):
     return render(request, "AdminPages/Admin_Dashboard.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")


def admin_master(request):
    # if request.session.has_key('aid'):
     return render(request, "AdminPages/AdminMaster.html")
    # else:
    #     return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")

def blood_stock(request):
    if request.session.has_key('aid'):
     return render(request, "AdminPages/Blood_Stock.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")



def manage_donors(request):
    if request.session.has_key('aid'):
     return render(request, "AdminPages/Manage_Donors.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")


def manage_request(request):
    if request.session.has_key('aid'):
     return render(request, "AdminPages/Manage_Requests.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")


def reports_analytics(request):
    if request.session.has_key('aid'):
     return render(request, "AdminPages/Reports_Analytics.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")


def change_password(request):

    if request.method == "POST":

        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            return HttpResponse(
                "<script>alert('Passwords do not match');window.location.href='/change_password/'</script>"
            )
        else:
         aid=request.session['aid']
         data=LoginModel.objects.get(email=aid)
         data.password=new_password
         data.save()

         return HttpResponse(
            "<script>alert('Password Changed Successfully');window.location.href='/Setting/'</script>"
        )

    return render(request, "AdminPages/ChangePassword.html")

# Settings Page
def settings(request):
    return render(request, "AdminPages/Settings.html")

