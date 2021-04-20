from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  



questions = [
    {
        'id': idx,
        'title': f'Title number {idx}',
        'text': f'Some text for question #{idx}',
        'tag': 'blabla'
    } for idx in range(10)
]




def index(request):
    return render(request,'index.html',{'questions': questions})

def hot_questions(request):
    return render(request, 'hot_questions.html', {'questions': questions})

def ask_question(request):
    return render(request, 'ask_question.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})


def one_question(request,pk):
    question=questions[pk]
    return render(request, 'question.html', {'question':question})

def tag(request,arg):
    tag_questions=filter(lambda question:question['tag']==arg,questions)
    return render(request, 'tag.html', {'questions':tag_questions})

def paginate (objects_list, request, per_page=10):
    paginator = Paginator(object_list, per_page) 

    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, 'list.html', {'objects': objects})