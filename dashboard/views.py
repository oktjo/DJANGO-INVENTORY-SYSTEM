from django.shortcuts import render,redirect
from django.http import HttpResponse
#method for login permissions
from django.contrib.auth.decorators import login_required
#for crud
from . models import Product,Order
from . forms import productForm , OrderForm
from django.contrib.auth.models import User
#messages
from django.contrib import messages

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
           instance= form.save(commit=False) #commit helps to view who made request in admn section
           instance.staff=request.user
           instance.save()
           return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {'orders':orders,
    'form':form,}
    return render(request,'dashboard/index.html',context)




#getting all admin users
@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context={'workers':workers}
    return render(request,'dashboard/staff.html',context)

def staff_detail(request,pk):
    worker = User.objects.get(id=pk)
    context={'worker':worker,}
    return render(request,'dashboard/staff_detail.html',context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    context ={'orders':orders}
    return render(request, 'dashboard/order.html',context)

@login_required(login_url='user-login')
def products(request):
    items = Product.objects.all()
    #items = product.objects.raw('SELECT * FROM dashboard_product')
    if request.method =='POST':
        form = productForm(request.POST)
        if form.is_valid():
           form.save()
           product_name = form.cleaned_data.get('name')
           messages.success(request, f'{product_name} has been succefully added')
           return redirect('dashboard-product')
    else:
        form = productForm()
    context = {'items':items, 'form':form}
    return render(request, 'dashboard/product.html',context)


@login_required(login_url='user-login')
def product_delete(request, pk):
    item =Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')


@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = productForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = productForm(instance=item)
        context={'form':form}
    
    return render(request,'dashboard/product_update.html',context)



