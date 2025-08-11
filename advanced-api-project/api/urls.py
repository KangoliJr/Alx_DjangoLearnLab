from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    # retrieving books and creating books
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    # retrieving updating and deleting a certain book
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail-update-delete')
    
]
