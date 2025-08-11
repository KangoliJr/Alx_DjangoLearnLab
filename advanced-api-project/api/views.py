from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BookSerializer
from .models import Book
# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # custom creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class  BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    