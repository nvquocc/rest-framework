from django.shortcuts import render
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializers import BookSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()  # show toan bo data
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

    # booksPython = list(books.values())
    # return JsonResponse({
    #     'books': booksPython
    # })  # tra ve ket qua dang json
