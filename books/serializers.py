from rest_framework import serializers
from .models import Book
from rest_framework.validators import ValidationError

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitob oldin ro'yxatdan o'tgan!"
                }
            )
        
        return data