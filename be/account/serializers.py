from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'real_name', 'phone_number', 'address', 'detail_address', 'posts_count', 'get_userimage', 'user_image', 'is_seller')

    
class UserSerializerNoIMG(serializers.ModelSerializer) :

    class Meta :
        model = User
        fields = ('id', 'name', 'email', 'real_name', 'phone_number', 'address', 'detail_address', 'is_seller')