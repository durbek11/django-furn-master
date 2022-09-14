
from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from .form import *
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    
    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)


    if 'product' in request.GET:
        search = request.GET['product']
        full_search = Q(Q(title__icontains=search) | Q(Q(price__icontains=search)))
        products = Product.objects.filter(full_search)
    else:
        products = Product.objects.all()

    
    if request.method  == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('furn:succses')
    else:
        form = ContactForm()
    base = Carousel.objects.all()
    blog = Blog.objects.all()
    categires = Category.objects.all()
    context = {
        "base": base, 
        "arrivals":arrivals, 
        "blog":blog,
        "products":products, 
        "categoryes":categires,
        "form":form
    }
    return render(request, 'pages/home.html', context)  



def arrivals_detail(request, pk):
    arrivals_detalis = Arrival.objects.get(id=pk)

    context ={
        "arrivals_detalis":arrivals_detalis
    }

    return render(request, "detalis/arrivals_detalis.html", context)

# ro`yhatdan o`tish qismi

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    
    return render(request, 'registration/signup.html', {"form":form})



def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                          request.FILES,
                                          instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("/profile/")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context ={
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, 'pages/profile.html', context)


class SuccsesView(generic.TemplateView):
    template_name = "pages/succses.html"
    # rate-star
def home(request):
    rate = RateStar.objects.filter(score=2).order_by("?").first()
    context = {
        "rate": rate
    }
    return render(request, "pages/star.html", context )

def rate_img(request):
    if request.method == "POST":
        el_id = request.POST.get("el_id")
        val = request.POST.get("val")
        rate = RateStar.objects.get(id=el_id)
        rate.score = val
        rate.save()
        return JsonResponse({"success": "true", "score": val}, safe=False)
    return JsonResponse({"success": "false"})
