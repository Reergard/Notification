from django.urls import path
from .views import book_create, edit_chapter, setting_book, BookSearchView, TitleAutocompleteView, BookAjaxSearchView,  GenresAutocompleteView, TagsAutocompleteView, FandomAutocompleteView, BookAdultAutocompleteView, BookNotAdultAutocompleteView
from .forms import TagAutocomplete, FandomAutocomplete, CountryAutocomplete, GenresAutocomplete
from .views import (
    Catalog, BookBase, TagList, TagDetail, GenresList, GenresDetail, FandomList, FandomDetail, CountryList, CountryDetail, ChapterCreate, ChapterDetail)
from .views import become_translator, become_freelancer
from .views import change_group, NotificationListAPIView
from . import views
from django.http import HttpResponse

app_name = 'catalog'

urlpatterns = [
    ...
    path('api/notifications/', NotificationListAPIView.as_view(), name='notification-list'),
]
