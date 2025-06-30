from rest_framework import serializers
from modelFood.models import Food
from models.models import Contact

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'  # Serialize all fields of the Food model

class ContactSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = '__all__'