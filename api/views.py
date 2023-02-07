from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class my_login(View):
    def get(self,rquest):
        return JsonResponse({"message":"success GET"})
    
    def post(self, request, *args, **kwargs):
        jd = json.loads(request.body)
        user = authenticate(request, username=jd["username"], password=jd["password"])
        if user is not None:
            # print(user.)
            user_data = {
                "id":user.id,
                'username':user.username,
            }
            return JsonResponse({'message': 'success',"user":user_data}, status=200)
        else:
            return JsonResponse({'message': 'Login failed'},status=401 )

class my_signup(View):
    def get(self,rquest):
        return JsonResponse({"message":"success GET signup"})
    
    def post(self, request, *args, **kwargs):
        try:
            jd = json.loads(request.body)
            user = User.objects.create_user(username=jd['username'], password=jd['password'])
            user.save()
            return JsonResponse({'message': 'User created successfully'})
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)




