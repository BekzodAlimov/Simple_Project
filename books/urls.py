from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListAPI, BookCreateAPI, BookDetailAPI, BookUpdateAPI, BookViewSet


router = SimpleRouter()
router.register('books',BookViewSet, basename='books')

urlpatterns = [
    # path('',BookListAPI.as_view()),
    # path('create/', BookCreateAPI.as_view()),
    # path('<int:pk>/',BookDetailAPI.as_view()),
    # path('<int:pk>/update/', BookUpdateAPI.as_view()),

    # #List Create URL
    # path('',BookListCreateAPI.as_view()),
    # path('',BookListAPI.as_view()),
    # path('create/', BookCreateAPI.as_view()),

    # #Update Delete URL
    # path('<int:pk>/',BookUpdateDeleteAPI.as_view()),
    # path('<int:pk>/',BookDetailAPI.as_view()),
    # path('<int:pk>/update/', BookUpdateAPI.as_view()),
    # path('<int:pk>/delete/', BookDeleteAPI.as_view()),
    
    # #for function
    # path('books1/', booklist),
]

urlpatterns = urlpatterns + router.urls