from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class BookListAPI(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status":f"Returned books : {len(books)}",
            "books":serializer_data
        } 

        return Response(data)
    

class BookCreateAPI(APIView):

    def post(self, request):
        data = request.data
        serializer_data = BookSerializer(data=data)
        if serializer_data.is_valid(raise_exception=True):
            serializer_data.save()
            data = {
                "status":f"Books are saved to database!",
                "data":data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        
class BookDetailAPI(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status":"Successful",
                "book":serializer_data
            }

            return Response(data)
        except Exception:
            data = {
                "status":"Failed",
                "message":"Book is not found!"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class BookDeleteAPI(APIView):
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            data = {
                "status":True,
                "message":"Successfully deleted!"
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            data = {
                "status":False,
                "message":"Boook is not found!"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        

class BookUpdateAPI(APIView):

    def put(self, request, pk):
        book = generics.get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer_data = BookSerializer(instance=book, data=data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
            serializer_data.save()
            data = {
                "status":True,
                "message":"Book is updated successfully!"
            }
            return Response(data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





# Create List API
# class BookListCreateAPI(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreateAPI(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookListAPI(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# @api_view(['GET'])
# def booklist(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)




# # Update, Retrieve, Delete API
# class BookUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookUpdateAPI(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDeleteAPI(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookDetailAPI(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer