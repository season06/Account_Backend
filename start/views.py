from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from collections import OrderedDict


from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from .models import *
from .serializers import *

from django.db.models import Sum, Count

# Query -> Dictionary
    # parms = ['A','B','C']
    # dict = list(query.values(*parms))
# Dictionary -> JSON
    # kpi_json = resp_Format(dict_items ,'group_category' ,['group_category'])

def resp_Format(list_content, index, fir_col):
	assert isinstance(list_content, list)
	assert isinstance(index, str)
	assert isinstance(fir_col, list)

	result_dict = {}
	for _dict in list_content:
		result_fields = {}
		index_name = _dict[index]
		for key, val in _dict.items():
			if not result_dict.get(index_name, {}):
				result_dict[index_name] = {}
				result_dict[index_name]['fields'] = []

			if key not in fir_col:
				result_fields[key] = val
			else:
				result_dict[index_name][key] = val

		sub_key = list(result_fields.keys())
		if len(sub_key) == 1:
			result_dict[index_name]['fields'].append(result_fields[sub_key[0]])
		else:
			result_dict[index_name]['fields'].append(result_fields)

	return [result_dict[key] for key in result_dict.keys()]

# class Data_Content(object, form, date, type_name):
#     self.form = form
#     self.date = date
#     self.type_name = type_name

#     self.category = {}
#     self.category['item'] = self.get_item
#     self.category['balance'] = self.get_balance

#     def get_item(self, date, type_name):
#         pass

#     def get_balance(self, date, type_name):
#         pass
#     def result(self):
#         return self.category[self.form](self.date, self.type_name)

class type_category(APIView):
    def get(self, request):
        query = Category.objects.all()
        category = [ _obj.item_type for _obj in query]

        return JsonResponse(category, safe=False)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        serializer.save()
        
        return JsonResponse(serializer.data, status=201)
        
    def delete(self, request):
        # print(request.META.get('CONTENT_TYPE', ''))
        # print(request.GET)
        # try:
        #     Category.objects.get(item_type = request.data.get('item_type'))
        # except Category.DoesNotExist:
        #     object_detail = Category(item_type=request.data.get('item_type'))
        #     object_detail.save()

        # object_detail = Category.objects.get(
        #         item_type = request.data.get('item_type', '')
        #     )

        get_args = {_key:_val[0] for _key,_val in dict(request.GET).items()}
        object_detail = Category.objects.get(
                    item_type = get_args['item_type']
                )

        if not object_detail:
            Response("Don't have this item_type", status=400)
        object_detail.delete()
        return Response('Delete sucess!')

class balance(APIView):
    def get(self, request):
        ARGS_PAR = [
        'date', # all(default) # YYYY-mm
        'type_name', # all(default) # type
		]
        get_args = {_key:_val[0] for _key,_val in dict(request.GET).items()}

        income_query = Charge.objects.filter(in_out_come='income')
        outcome_query = Charge.objects.filter(in_out_come='outcome')

        if(get_args['date'] != ''):
            date_split = get_args['date'].split('-') # [year, month]
            income_query = income_query.filter(date__year=date_split[0], date__month=date_split[1])
            outcome_query = outcome_query.filter(date__year=date_split[0], date__month=date_split[1])

        if(get_args['type_name'] != ''):
            income_query = income_query.filter(type_name=get_args['type_name'])
            outcome_query = outcome_query.filter(type_name=get_args['type_name'])

        income = income_query.aggregate(income=Sum('cost'))
        outcome = outcome_query.aggregate(outcome=Sum('cost'))
        dict_balance = {
            'income': income['income'],
            'outcome': outcome['outcome'],
            'total': income['income']-outcome['outcome']
        }
        return JsonResponse(dict_balance, safe=False)

class data_view(APIView):
    def get(self, request):
        ARGS_PAR = [
		'date', # now_time(default) # YYYY-mm
        'type_name', # all(default) # type
		]
        get_args = {_key:_val[0] for _key,_val in dict(request.GET).items()}

        now_time = datetime.now().strftime('%Y-%m')
        
        if(get_args['date'] == ''):
            date_split = now_time.split('-') # [year, month]
        else:
            date_split = get_args['date'].split('-') # [year, month]
        data_query = Charge.objects.filter(date__year=date_split[0], date__month=date_split[1])

        if(get_args['type_name'] != ''):
            data_query = data_query.filter(type_name=get_args['type_name'])

        serializer = ChargeSerializer(data_query, many=True)
        data = serializer.data

        return JsonResponse(data, safe=False)

    # def post(self, request):
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data, status=201)
    #     return JSONResponse(serializer.errors, status=400)

# -> url

"""
todo:
    編輯
    error exception_handling
"""
"""
home_page:
    get_item
    get_balance: income outcome total
    get_type
"""
"""
filter:
    get_type_name
    分類 總計
"""

"""
日 / 月
收入 支出 結餘

新增 編輯 刪除
"""


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer