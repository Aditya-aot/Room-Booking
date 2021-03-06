from django.shortcuts import render,redirect

from .models import room_book
from .forms import ChatForm 

# Create your views here.
def book_view(request) :

    form= ChatForm()
    # form2=ChatForm2()
    set_model = room_book.objects.all()
    seat_html = '' 
    seat_html2=''
    if request.method == 'POST':
            form = ChatForm(request.POST)

            if form.is_valid() :
                form.save()

                obj = form.save(commit=False)
                obj.user = request.user or None
                obj.save()
                return redirect('/done')

    # username = request.user
    # user_model = set_model.filter(user=username)

    for student in set_model:
        print(student.a101 )
        if student.a101==True :
            print('seat sold')
            seat_html='<!-- '
            seat_html2=' -->'


    context ={ 'form':form ,
                # 'form2':form2,
                'seat':seat_html,
                'seat2':seat_html2


                 }
    return render(request, 'book/book.html' ,context)



def done_view(request) :
    set_model = room_book.objects.all()
    username = request.user
    payment_data = set_model.filter(user = username)
    context = {'pay':payment_data,
    
                }
    return render(request, 'book/done.html' , context )


def home_view(request) :

    context = {}
    return render(request, 'free/index.html' , context )

def more_view(request) :

    context = {}
    return render(request, 'free/more.html' , context )

def boys_view(request) :

    context = {}
    return render(request, 'free/boysinfo.html' , context )


def girls_view(request) :

    context = {}
    return render(request, 'free/girlsinfo.html' , context )
