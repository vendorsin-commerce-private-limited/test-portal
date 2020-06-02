from django.db import models
from django.db.models import Model


# Create your models here.
class CountryModel(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(max_length=50, unique=True)
    country_prefix = models.CharField(max_length=50)
    country_currency = models.CharField(max_length=50)

    class Meta:
        db_table = "CountryModel"


class StateModel(models.Model):
    state_id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    state_code = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "StateModel"


class CityModel(models.Model):
    city_id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=50)
    city_code = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "CityModel"


class IndustryMaincoreModel(models.Model):
    maincore_id = models.BigAutoField(primary_key=True)
    maincore_name = models.CharField(max_length=50, unique=True)
    maincore_Code = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    maincore_created_on = models.DateTimeField(auto_now=True)
    maincore_created_by = models.BigIntegerField()
    maincore_modified_on = models.DateTimeField(auto_now_add=True)
    maincore_modified_by = models.BigIntegerField()

    class Meta:
        db_table = 'IndustryMaincoreModel'


class IndustryCategoryModel(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    category_Code = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    maincore = models.ForeignKey(IndustryMaincoreModel, on_delete=models.CASCADE)
    category_created_on = models.DateTimeField(auto_now=True)
    category_created_by = models.BigIntegerField()
    category_modified_on = models.DateTimeField(auto_now_add=True)
    category_modified_by = models.BigIntegerField()

    class Meta:
        db_table = "IndustryCategoryModel"


class IndustrySubCategoryModel(models.Model):
    sub_category_id = models.BigAutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=50, unique=True)
    sub_category_Code = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    category = models.ForeignKey(IndustryCategoryModel, on_delete=models.CASCADE)
    sub_category_created_on = models.DateTimeField(auto_now=True)
    sub_category_created_by = models.BigIntegerField()
    sub_category_modified_on = models.DateTimeField(auto_now_add=True)
    sub_category_modified_by = models.BigIntegerField()

    class Meta:
        db_table = "IndustrySubCategoryModel"
