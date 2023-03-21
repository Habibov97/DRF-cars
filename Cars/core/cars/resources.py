from import_export import resources
from cars.models import CarSeries

class CarsResource(resources.ModelResource):

    class Meta:
        model = CarSeries