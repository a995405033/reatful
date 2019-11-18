
from sqLite3 import models
from rest_framework import viewsets
from sqLite3.ret_serizlizer import BookSerializer#从序列化文件调用
from sqLite3.ret_serizlizer import AuthorSerializer#从序列化文件调用


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()   #变量名必须嘚这么写
    serializer_class = BookSerializer



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()   #变量名必须嘚这么写
    serializer_class = AuthorSerializer