from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Band, Member
from .forms import BandContactForm


def home(request):
    return render(request, 'home.html')


def band_listing(request):
    """ A view of all bands. """
    bands = Band.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        bands = bands.filter(name__icontains=var_get_search)
    return render(request, 'bands/band_listing.html', {'bands': bands})


def band_contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact.html', {'form': form})


def band_detail(request, pk):
    """ A view of all members by bands. """
    band = Band.objects.get(pk=pk)
    members = Member.objects.all().filter(band=band)
    context = {'members': members, 'band': band}
    return render(request, 'bands/band_detail.html', context)


class BandForm(CreateView):
    template_name = 'bands/band_form.html'
    model = Band
    success_url = reverse_lazy('bands')


class MemberForm(CreateView):
    template_name = 'bands/member_form.html'
    model = Member
    success_url = reverse_lazy('bands')


@login_required(login_url='/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'bands/protected.html', {'current_user': request.user})


def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')
