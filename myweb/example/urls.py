from django.urls import path, include
from .views import HelloAPI, BookAPI, BooksAPI, bookAPI, booksAPI, BookAPIMixins, BooksAPIMixins, BookViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>", BookAPI.as_view()),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view())
]