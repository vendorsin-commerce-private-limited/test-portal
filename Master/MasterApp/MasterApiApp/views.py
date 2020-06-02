from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from MasterApiApp.models import CountryModel
from MasterApiApp.models import StateModel
from MasterApiApp.models import CityModel
from MasterApiApp.models import IndustryMaincoreModel
from MasterApiApp.models import IndustryCategoryModel
from MasterApiApp.models import IndustrySubCategoryModel


class CountryView(APIView):

    def post(self, request):
        data = request.data
        try:
            for d in data:
                country_posted = CountryModel.objects.update_or_create(
                    country_name=d['country_name'],
                    country_code=d['country_code'],
                    defaults={
                        'country_prefix': d['country_prefix'],
                        'country_currency': d['country_currency']}
                )
            return Response({'status': 201, 'message': "Success"}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def get(self, request):
        data = request.data

        try:
            # countries = CountryModel.objects.filter(country_id=data['country_id']).values()
            countries = CountryModel.objects.all().values()
            return Response({'status': 201, 'message': "Success", "data": countries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def put(self, request):
        data = request.data

        try:
            countriesbyid = CountryModel.objects.filter(country_id=data['country_id']).values()
            countries = CountryModel.objects.get(country_id=data['country_id'])
            country_name = data['country_name']
            country_code = data['country_code']
            country_prefix = data['country_prefix']
            country_currency = data['country_currency']

            if countries.country_name != country_name:
                countries.country_name = country_name
                countries.save()
                return Response({'status': 201, 'message': "Success", "data": countriesbyid}, status=201)
            elif countries.country_code != country_code:
                countries.country_code = country_code
                countries.save()
                return Response({'status': 201, 'message': "Success", "data": countriesbyid}, status=201)
            elif countries.country_prefix != country_prefix:
                countries.country_prefix = country_prefix
                countries.save()
                return Response({'status': 201, 'message': "Success", "data": countriesbyid}, status=201)
            elif countries.country_currency != country_currency:
                countries.country_currency = country_currency
                countries.save()
                return Response({'status': 201, 'message': "Success", "data": countriesbyid}, status=201)
            else:
                return Response({'status': 500, 'message': "data already present"}, status=500)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def delete(self, request):
        data = request.data

        try:
            countries = CountryModel.objects.get(country_id=data['country_id'])
            countries.delete()
            return Response({'status': 201, 'message': "Success", "data": countriesbyid}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

            # try:
        #     Country_Name=data['Country_Name']
        #     countries = CountryModel.objects.get(Country_Name=data['Country_Name'])
        #     selectedID=data['selectedID']
        #     if countries.id == selectedID:
        #         countriesbyid = CountryModel.objects.filter(id=data['id']).values()
        #         return Response({'status':201, 'message':"success", "data":countriesbyid},status=201)
        #     else:
        #         countriesbycountryname = CountryModel.objects.filter(Country_Name=data['Country_Name']).values()
        #         return Response({'status':201, 'message':"success", "data":countriesbycountryname},status=201)
        # except Exception as e:
        #     return Response({'status':500,'error':str(e)},status=500)

        # countries = CountryModel.objects.all()
        # serialized_data = CountrySerializer(queryset=countries, many=True).data
        # data = []
        # if serialized_data.is_valid():
        #     data = serialized_data.data
        # return Response({'status':201, 'message':"success", "data":countries},status=201)


# ---------------------------------------------------------------------------------------------------------

class StateView(APIView):
    def post(self, request):
        data = request.data
        try:
            for d in data:
                states_posted = StateModel.objects.create(
                    state_name=d['state_name'],
                    state_code=d['state_code'],
                    country=CountryModel.objects.get(country_id=d['country_id']))
            return Response({'status': 201, 'message': "Success"}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def get(self, request):
        data = request.data

        try:
            statesbyid = StateModel.objects.filter(country_id=data['country_id']).values()
            return Response({'status': 201, 'message': "success", "data": statesbycountry}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def put(self, request):
        data = request.data

        try:
            statesbyid = StateModel.objects.filter(state_id=data['state_id']).values()
            states = StateModel.objects.get(state_id=data['state_id'])
            state_name = data['state_name']
            state_code = data['state_code']
            country = data['country']

            if states.state_name != state_name:
                states.state_name = state_name
                states.save()
                return Response({'status': 201, 'message': "Success", "data": statesbyid}, status=201)
            elif states.state_code != state_code:
                states.state_code = state_code
                states.save()
                return Response({'status': 201, 'message': "Success", "data": statesbyid}, status=201)
            else:
                return Response({'status': 500, 'message': "data already present"}, status=500)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def delete(self, request):
        data = request.data
        try:
            statesbyid = StateModel.objects.filter(state_id=data['state_id']).values()
            states = StateModel.objects.get(state_id=data['state_id'])
            states.delete()
            return Response({'status': 201, 'message': "Success", "data": statesbyid}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

            # def get(self,request):
    #     data = request.data
    #     states = StateModel.objects.filter(country_id=data['country_id']).values('state_name','state_id')
    #     return Response({'status':201, 'message':"success", "data":states},status=201)

    # myCountryName=data['CountryName']
    # data = request.data
    # one_entry = CountryModel.objects.get(pk=1)
    # if one_entry.Country_Name == myCountryName:
    #     one_entry.Country_Name = "France"
    #     one_entry.save()
    #     return Response({'status':201, 'message':"success"},status=201)

    # data = request.data
    # CountryName=data['CN']
    # countryserachbyname =CountryModel.objects.filter(Country_Name=CountryName)
    # if countryserachbyname.Country_Name == CountryName:
    # value=one_entry.json()
    # print(value)


# ---------------------------------------------------------------------------------------------------------

class CityView(APIView):
    def post(self, request):
        data = request.data
        try:
            for d in data:
                state_posted = CityModel.objects.create(
                    city_name=d['city_name'],
                    city_code=d['city_code'],
                    state=StateModel.objects.get(state_id=d['state_id']))
            return Response({'status': 201, 'message': "Success"}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def get(self, request):
        data = request.data

        try:
            cities = CityModel.objects.filter(state_id=data['state_id']).values()
            return Response({'status': 201, 'message': "success", "data": cities}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def put(self, request):
        data = request.data

        try:
            citiesbyid = CityModel.objects.filter(city_id=data['city_id']).values()
            cities = CityModel.objects.get(city_id=data['city_id'])
            city_name = data['city_name']
            city_code = data['city_code']

            if cities.city_name != city_name:
                cities.city_name = city_name
                cities.save()
                return Response({'status': 201, 'message': "Success", "data": citiesbyid}, status=201)
            elif cities.city_code != city_code:
                cities.city_code = city_code
                cities.save()
                return Response({'status': 201, 'message': "Success", "data": citiesbyid}, status=201)
            else:
                return Response({'status': 500, 'message': "data already present"}, status=500)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def delete(self, request):
        data = request.data
        try:
            citiesbyid = CityModel.objects.filter(city_id=data['city_id']).values()
            cities = CityModel.objects.get(city_id=data['city_id'])
            cities.delete()
            return Response({'status': 201, 'message': "Success", "data": citiesbyid}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

# -------------------------------------------------------------------------------------------------------


class IndustryMaincoreView(APIView):
    def post(self, request):
        data = request.data
        try:
            for d in data:
                industries_posted = IndustryMaincoreModel.objects.create(maincore_name=d['maincore_name'],
                                                                         maincore_Code=d['maincore_Code'],
                                                                         maincore_created_by=d['maincore_created_by'],
                                                                         maincore_modified_by=d['maincore_modified_by'])
            return Response({'status': 201, 'message': "Success"}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def get(self, request):
        data = request.data

        try:
            industries = IndustryMaincoreModel.objects.filter(maincore_id=data['maincore_id']).values()
            return Response({'status': 201, 'message': "success", "data": industries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def put(self, request):
        data = request.data

        try:
            industries = IndustryMaincoreModel.objects.filter(maincore_id=data['maincore_id']).values()
            industriesbyid = IndustryMaincoreModel.objects.get(maincore_id=data['maincore_id'])
            maincore_name = data['maincore_name']
            maincore_Code = data['maincore_Code']
            maincore_created_by = data['maincore_created_by']
            maincore_modified_by = data['maincore_modified_by']

            if industriesbyid.maincore_name != maincore_name:
                industriesbyid.maincore_name = maincore_name
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.maincore_Code != maincore_Code:
                industriesbyid.maincore_Code = maincore_Code
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.maincore_created_by != maincore_created_by:
                industriesbyid.maincore_created_by = industriesbyid.maincore_created_by
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.maincore_modified_by != maincore_modified_by:
                industriesbyid.maincore_modified_by = maincore_modified_by
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            else:
                return Response({'status': 500, 'message': "data already present"}, status=500)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def delete(self, request):
        data = request.data
        try:
            industries = IndustryMaincoreModel.objects.filter(maincore_id=data['maincore_id']).values()
            industriesbyid = IndustryMaincoreModel.objects.get(maincore_id=data['maincore_id'])
            industriesbyid.delete()
            return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)


# ---------------------------------------------------------------------------------------------------------


class IndustryCategoryView(APIView):
    def post(self, request):
        data = request.data
        try:
            for d in data:
                industries_category_posted = IndustryCategoryModel.objects.create(category_name=d['category_name'],
                                                                                  category_Code=d['category_Code'],
                                                                                  # maincore_id =d['maincore_id'],
                                                                                  maincore=IndustryMaincoreModel.objects.get(
                                                                                      maincore_id=d['maincore_id']),
                                                                                  category_created_by=d[
                                                                                      'category_created_by'],
                                                                                  category_modified_by=d[
                                                                                      'category_modified_by'])
            return Response({'status': 201, 'message': "Success"}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def get(self, request):
        data = request.data

        try:
            industries = IndustryCategoryModel.objects.filter(maincore_id=data['maincore_id']).values()
            return Response({'status': 201, 'message': "success", "data": industries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)


    def put(self, request):
        data = request.data

        try:
            industries = IndustryCategoryModel.objects.filter(category_id=data['category_id']).values()
            industriesbyid = IndustryCategoryModel.objects.get(category_id=data['category_id'])
            category_name = data['category_name']
            category_Code = data['category_Code']
            category_created_by = data['category_created_by']
            category_modified_by = data['category_modified_by']

            if industriesbyid.category_name != category_name:
                industriesbyid.category_name = category_name
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.category_Code != category_Code:
                industriesbyid.category_Code = category_Code
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.category_created_by != category_created_by:
                industriesbyid.category_created_by = industriesbyid.category_created_by
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.category_modified_by != category_modified_by:
                industriesbyid.category_modified_by = maincore_modified_by
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            else:
                return Response({'status': 500, 'message': "data already present"}, status=500)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def delete(self, request):
        data = request.data
        try:
            industries = IndustryCategoryModel.objects.filter(category_id=data['category_id']).values()
            industriesbyid = IndustryCategoryModel.objects.get(category_id=data['category_id'])
            industriesbyid.delete()
            return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

# ----------------------------------------------------------------------------------------------------------------------

class IndustrySubCategoryView(APIView):
    def post(self, request):
        data = request.data
        try:
            for d in data:
                industries_sub_category_posted = IndustrySubCategoryModel.objects.create(
                    sub_category_name=d['sub_category_name'],
                    sub_category_Code=d['sub_category_Code'],
                    category=IndustryCategoryModel.objects.get(category_id=d['category_id']),
                    category_created_by=d['category_created_by'],
                    sub_category_modified_by=d['sub_category_modified_by'])
            return Response({'status': 201, 'message': "Success"}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def get(self, request):
        data = request.data

        try:
            industries = IndustrySubCategoryModel.objects.filter(category_id=data['category_id']).values()
            return Response({'status': 201, 'message': "success", "data": industries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)



    def put(self, request):
        data = request.data

        try:
            industries = IndustrySubCategoryModel.objects.filter(sub_category_id=data['sub_category_id']).values()
            industriesbyid = IndustrySubCategoryModel.objects.get(sub_category_id=data['sub_category_id'])
            sub_category_name = data['sub_category_name']
            sub_category_Code = data['sub_category_Code']
            sub_category_created_by = data['sub_category_created_by']
            sub_category_modified_by = data['sub_category_modified_by']

            if industriesbyid.sub_category_name != sub_category_name:
                industriesbyid.sub_category_name = sub_category_name
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.sub_category_Code != sub_category_Code:
                industriesbyid.sub_category_Code = sub_category_Code
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.sub_category_created_by != sub_category_created_by:
                industriesbyid.sub_category_created_by = industriesbyid.sub_category_created_by
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            elif industriesbyid.sub_category_modified_by != sub_category_modified_by:
                industriesbyid.sub_category_modified_by = sub_category_modified_by
                industriesbyid.save()
                return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
            else:
                return Response({'status': 500, 'message': "data already present"}, status=500)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

    def delete(self, request):
        data = request.data
        try:
            industries = IndustrySubCategoryModel.objects.filter(sub_category_id=data['sub_category_id']).values()
            industriesbyid = IndustrySubCategoryModel.objects.get(sub_category_id=data['sub_category_id'])
            industriesbyid.delete()
            return Response({'status': 201, 'message': "Success", "data": industries}, status=201)
        except Exception as e:
            return Response({'status': 500, 'error': str(e)}, status=500)


