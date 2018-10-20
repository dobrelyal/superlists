from django.shortcuts import redirect, render
from lists.models import Item, List
#from django.http import HttpResponse
# Create your views here.
def home_page(request):
    '''домашняя страница'''
    return render(request, 'home.html')

def new_list(request):
    '''новый список'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')


def view_list(request):
    '''существующий список'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
