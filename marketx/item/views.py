from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,get_object_or_404, redirect
from .models import Items,Category
from .forms import NewItemForm, EditItemForm
# Create your views here.

def items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    items=Items.objects.filter(is_sold=False)
    categories=Category.objects.all()
    if query:
        items=items.filter(Q(name__icontains=query)|Q(description__icontains=query))
    if category_id:
        items=items.filter(category_id=category_id)
    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'category':categories,
        'category_id':int(category_id),
    })

def detail(request,pk):
    item=get_object_or_404(Items,pk=pk)
    related_items =Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        "item":item,
        "related_items":related_items
    }
                  )

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
        else:
            form=NewItemForm()

    form=NewItemForm()
    return render(request, 'item/form.html',{
        'form':form,
        'title': 'New Item',
    })

@login_required
def edit(request,pk):
    item=get_object_or_404(Items, pk=pk , created_by=request.user)
    if request.method=='POST':
        form=EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
        else:
            form=EditItemForm()

    form=EditItemForm()
    return render(request, 'item/form.html',{
        'form':form,
        'title': 'New Item',
    })
    

@login_required
def delete(request, pk):
    item=get_object_or_404(Items, pk=pk , created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

