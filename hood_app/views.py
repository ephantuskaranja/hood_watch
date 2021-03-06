from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reports, Recommendation, Hood
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, ReportForm, RecommendationsForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.
@login_required
def index(request):
    Recs=Recommendation.objects.all()[:5]
    Reps=Reports.objects.all()[:5]
    context={
        "title":'Neighbourhood watch',
        "Recs":Recs,
        "Reps":Reps
    }

    
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def get_reports(request):
    reps=Reports.objects.all()
    context = {
        "reps":reps,
    }
    
    return render(request, 'reports.html', context)

@login_required
def get_recommendations(request):
    recs=Recommendation.objects.all()
    context = {
        "recs":recs,
    }
    
    return render(request, 'recommendations.html', context)


@login_required
def makeReport(request):
    current_user = request.user
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report=form.save(commit=False)
            report.user = current_user
            report.save()
            return HttpResponseRedirect('/')

    else:
        form = ReportForm()
   
    
    return render(request, 'makeReport.html',{"form":form})


@login_required
def makeRecommendations(request):
    current_user = request.user
    if request.method == 'POST':
        form = RecommendationsForm(request.POST)
        if form.is_valid():
            recommendation =form.save(commit=False)
            recommendation.user = current_user
            recommendation.save()
            return HttpResponseRedirect('/')

    else:
        form = RecommendationsForm()
   
    
    return render(request, 'makeRecommendations.html',{"form":form})


