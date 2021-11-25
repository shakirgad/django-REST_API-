from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics , mixins
from rest_framework import status,filters

#get operation using generic
class Book_Class_Api(generics.ListAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
#post and get using mixins
class Bookmixins_list(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def get(self , request):
        return self.list(request)
    def post(self ,request):
        return self.create(request)
 
#get ,delete,update       
class Bookmixins_up_des(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self , request,pk):
        return self.retrieve(request)
    def delete(self ,request,pk):
        return self.destroy(request)
    def put(self ,request,pk):
        return self.update(request)
   