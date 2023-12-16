from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Items

# Create your views here.
@login_required
def index(request):
    items=Items.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html',{
        'items':items,
    })


