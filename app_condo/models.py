from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_condo_district'


class Subdistrict(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='subdistricts')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_condo_subdistrict'


class NearestRoad(models.Model):
    name = models.CharField(max_length=100)
    subdistrict = models.ForeignKey(Subdistrict, on_delete=models.CASCADE, related_name='nearest_roads')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_condo_nearestroad'


class CondoPricePrediction(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    price_per_square_meter = models.FloatField()
    # Other fields as necessary...

    class Meta:
        db_table = 'app_condo_price_prediction'
