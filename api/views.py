from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate

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
        return JsonResponse({"message":"success GET signup"})



