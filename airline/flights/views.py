from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist



from .models import Flight
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except ObjectDoesNotExist:
        return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
        "Error": True,
        })
    else:
        return render(request, "flights/flight.html", {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "Error": False,
        })
