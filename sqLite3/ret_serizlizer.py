from sqLite3.models import Book
from sqLite3.models import Author
from rest_framework import serializers


# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer): # ModelSerializer 看到外键ID
    class Meta:
        model = Book
        depth = 2       #显示2层
        fields = ['url', 'price', 'author', ]


#如果是外键字段 要重新创建一个新的类
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['authorname']
