from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from furnapp.models import *
from django.db.models import Q
from django.utils import timezone
from django.db.models import Avg

User = get_user_model()

bugun = timezone.now().astimezone()


def home(request):
    contact_last = Contact.objects.filter(date__date=timezone.now()).count() # timezone.now()  bu yerga agar " - timezone.timedelta(1) qo`shilsa bir kun oldingi kelgan xabarlari ko`rsatadi."
    contact = Contact.objects.all().order_by('-id')[:contact_last]
    contact_count = Contact.objects.count()
    conatc_taklif = Contact.objects.filter(choices="Taklif").count() #Bu yerdagi (choices="Taklif") furnappdagi models.py Contact TAKLIF = "Taklif" 
    contact_shikoyat = Contact.objects.filter(choices="Shikoyat").count()
    users = User.objects.count()
    products = Product.objects.count()
    blog =  Blog.objects.count()
    arravial = Arrival.objects.count()
    avg_rate = Product.objects.aggregate(Avg("score"))
    context = {
        "avg_rate":avg_rate,
        "contact_count":contact_count,
        "contact_last":contact_last,
        "contact":contact,
        "contact_taklif":conatc_taklif,
        "contact_shikoyat":contact_shikoyat,
        "users":users,
        "products":products,
        "blogs":blog,
        "arravials":arravial
    }
    return render(request, 'dashboard/pages/home.html', context)

def contact_full(request, pk):
    contacts = Contact.objects.get(id=pk)
    context ={
        "contacts":contacts
    }
    return render(request, "dashboard/pages/contacts.html", context)

class Buttons(generic.TemplateView):
   template_name ="dashboard/includes/buttons.html"

def cards(request):
    return render(request, 'dashboard/includes/cards.html')

def animation(request):
    return render(request, 'dashboard/includes/animation.html')

def colors(request):
    return render(request, 'dashboard/includes/colors.html')

def border(request):
    return render(request, 'dashboard/includes/border.html')

def other(request):
    return render(request, 'dashboard/includes/other.html')

def dashboard_login(request):
    return render(request, 'dashboard/registrations/login.html')

def forgot_password(request):
    return render(request, 'dashboard/includes/forgot-password.html')

def register(request):
    return render(request, 'dashboard/registrations/register.html')

def charts(request):
    return render(request, 'dashboard/includes/charts.html')

def tables(request):
    if 'user' in request.GET:
        search = request.GET['user']
        full_search = Q(Q(first_name__icontains=search) | Q(Q(email__icontains=search)))
        profile_search = Q(Q(mobile_number__icontains=search))
        user = User.objects.filter(full_search)
        profile = Profile.objects.filter(profile_search)
    else:
        user = User.objects.all()
    context={
        "user_full":user
    }
    return render(request, 'dashboard/includes/tables.html', context)

def page_404(request):
    return render(request, 'dashboard/includes/404.html')

def blank(request):
    return render(request, 'dashboard/includes/blank.html')


