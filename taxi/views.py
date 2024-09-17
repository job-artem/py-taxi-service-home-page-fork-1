from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request):
    return render(
        request,
        context={
            "num_drivers": Driver.objects.count(),
            "num_manufacturers": Driver.objects.count(),
            "num_cars": Car.objects.count()
        },
        template_name="taxi/index.html"
    )
