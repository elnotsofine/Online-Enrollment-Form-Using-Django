from django.shortcuts import render, redirect

# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # allow ANY username/password as long as not blank
        if username and password:
            request.session["user"] = username
            return redirect("dashboard")

        return render(request, "login.html", {"error": "All fields are required."})

    return render(request, "login.html")


# DASHBOARD VIEW
def dashboard(request):
    if "user" not in request.session:
        return redirect("login")
    return render(request, "dashboard.html")


# TABS
def student_data(request):
    return render(request, "student_data.html")

def personal_info(request):
    return render(request, "personal_info.html")

def educational_bg(request):
    return render(request, "educ_background.html")

def family_bg(request):
    return render(request, "family_background.html")

def schedule(request):
    return render(request, "schedule.html")


# LOGOUT
def logout_view(request):
    request.session.flush()
    return redirect("login")
