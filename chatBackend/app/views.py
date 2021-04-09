from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,Message
from .serializers import UserSerializer,MessageSerializer

def validateUser(request):
    email=request.GET['email']
    pas=request.GET['pas']
    try:
        obj=User.objects.get(email=email)
        if obj.password==pas:
            return JsonResponse({'status':True,'id':obj.id,'name':obj.name})
        else:
            return JsonResponse({'status':"Wrong pass"})
    except:
        return JsonResponse({'status':"User not found"})

def userData(request):
    serialize=User.objects.all()
    data=UserSerializer(serialize,many=True)
    return JsonResponse(data.data,safe=False)

def msgData(request,convo):
    serialize=Message.objects.filter(convo=convo)
    data=MessageSerializer(serialize,many=True)
    return JsonResponse(data.data,safe=False)
