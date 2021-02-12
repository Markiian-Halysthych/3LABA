
from django.shortcuts import render,redirect
from .models import Car
from .forms import CarForm
from django.views.generic import UpdateView,DeleteView

def view_page(request):
    car=Car.objects.order_by('-price')
    return render(request,'main\View Page.html', {'car':car})


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'main\Edit Page.html'
    form_class = CarForm

class CarDeleteView(DeleteView):
    model = Car
    success_url = '/'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def create_page(request):
    error= False
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
        else:
            error=True

    form = CarForm()
    date = {
        'form':form,
        'error':error
    }
    return render(request,'main\Create Page.html',date)

