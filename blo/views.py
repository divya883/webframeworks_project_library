from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blo.models import Book,BookInstance
# Create your views here.


def index(request):
	"""View function for home page of site."""

	# Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
    
	# Available books (status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
	# The 'all()' is implied by default.    
	#num_authors = Author.objects.count()
	
	num_visits=request.session.get('num_visits',0)
	request.session['num_visits']=num_visits+1
    
	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_visits':num_visits,
        
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
	model=Book

	
#class BookDetailView(generic.DetailView):
	#model=Book


def contact(request):
	return render(request,'contacts.html')

def education(request):
	return render(request,'education.html')

def fiction(request):
	return render(request,'fiction.html')

def nonfiction(request):
	return render(request,'nonfiction.html')


class BorrowedBooksByUserListView(LoginRequiredMixin, generic.ListView):
   
    model = BookInstance
    template_name = 'blo/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='b').order_by('due_back')

class Signup(generic.CreateView):
	form_class=UserCreationForm
	success_url=reverse_lazy('login')
	template_name='signup.html'

