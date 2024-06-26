from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializerNoIMG
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignupForm
from .models import User

@api_view(['GET'])
def me(request) :
    return JsonResponse({
        'id' : request.user.id,
        'name' : request.user.name,
        'email' : request.user.email,
        'real_name' : request.user.real_name,
        'phone_number' : request.user.phone_number,
        'address' : request.user.address,
        'detail_address' : request.user.detail_address,
        'user_image' : request.user.get_userimage(),
        'is_seller' : request.user.is_seller,
    })

@api_view(['GET'])
def me_noimg(request):
    serializers = UserSerializerNoIMG(request.user)
    return JsonResponse(serializers.data)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
        'real_name': data.get('real_name'),
        'phone_number' : data.get('phone_number'),
        'address' : data.get('address'),
        'detail_address' : data.get('detail_address'),
    })

    if form.is_vaild():
        form.save()
    else :
        messaage = form.errors.as_json()

    return JsonResponse({'message': message}, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editprofile(request):
    user = request.user
    name = request.data.get('name')
    real_name = request.data.get('real_name')
    address = request.data.get('address')
    detail_address = request.data.get('detail_address')

    if User.objects.exclude(id=user.id).filter(name=name).exists():
        return JsonResponse({'message': 'nickname already exists'})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editpassword(request):
    user = request.use

    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()
        return JsonResponse({'message' : 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)