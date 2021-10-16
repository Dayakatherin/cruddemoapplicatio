from rest_framework import serializers 
from demoapp.models import user
 
 
class userSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = user
        fields = ('id',
                  'first_name',
                  'last_name',
                  'user_name',
                  'email_id',
                  'password')