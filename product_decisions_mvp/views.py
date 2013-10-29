import logging
import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Bike

logger = logging.getLogger(__name__)

def detail(request, bike_id):

    bike = get_object_or_404(Bike, pk=bike_id)

    return render(request, 'detail.html', {'bike': bike})

def api_bikes_all(request):

    bikes = Bike.objects.all()

    def to_json(bike):
        return {
            "id": bike.pk,
            "title": bike.title,
            "price": bike.price,
            "riderHeightLowerTotalInches": bike.rider_height_lower_total_inches,
            "riderHeightUpperTotalInches": bike.rider_height_upper_total_inches,
            "male": bike.male,
            "female": bike.female,
            "primaryImgUrl": bike.primary_img_url
        }

    bikes = [to_json(bike) for bike in bikes]

    return HttpResponse(json.dumps(bikes), content_type="application/json")