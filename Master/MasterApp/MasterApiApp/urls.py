from django.urls import path
from MasterApiApp.views import CountryView
from MasterApiApp.views import StateView
from MasterApiApp.views import CityView
from MasterApiApp.views import IndustryMaincoreView
from MasterApiApp.views import IndustryCategoryView
from MasterApiApp.views import IndustrySubCategoryView

urlpatterns = [
    path('countryview', CountryView.as_view()),
    path('stateview', StateView.as_view()),
    path('cityview', CityView.as_view()),
    path('industry_maincore', IndustryMaincoreView.as_view()),
    path('industry_category', IndustryCategoryView.as_view()),
    path('industry_subcategory', IndustrySubCategoryView.as_view()),
]
