from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('books/',views.BookListView.as_view(),name='books'),
	path('contact/',views.contact,name='contact'),
	#path('book/<int:pk>',views.BookDetailView.as_view(),name='book-detail'),
	path('education/',views.education,name='education'),
	path('fiction/',views.fiction,name='fiction'),
	path('nonfiction/',views.nonfiction,name='nonfiction'),
	path('mybooks/',views.BorrowedBooksByUserListView.as_view(),name='my-borrowed'),
	path('signup/',views.Signup.as_view(),name='signup'),

]