from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import (
    About,
    Shop,
    Service,
    Blog,
)
from .forms import ShopForm, BlogForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmailForm


def about_list(request):
    about_items = About.objects.all()
    return render(request, 'about.html', {'about': about_items})


def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop.html', {'shops': shops})


def shop_detail(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    return render(request, 'shop_detail.html', {'shop': shop})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


class ContactView(TemplateView):
    template_name = 'gmail/contact.html'


class CreateViewShop(CreateView):
    form_class = ShopForm
    template_name = 'crud/create.html'
    success_url = reverse_lazy('shop')


class ShopDeleteView(DeleteView):
    model = Shop
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('shop')


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'crud/post_edit.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        project = form.save()
        return redirect(reverse('shop_detail', kwargs={'slug': project.slug}))


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'image', 'info']
    template_name = 'crud/create.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('blog')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'crud/post_edit.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        project = form.save()
        return redirect(reverse('blog_detail', kwargs={'pk': project.pk}))


def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            recipient = form.cleaned_data['recipient']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f'Message from {first_name} {last_name}',
                    message=message,
                    from_email='anonshack48@gmail.com',
                    recipient_list=[recipient],
                    fail_silently=False,
                )
                return render(request, 'gmail/success.html')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'An error occurred: {e}')
    else:
        form = EmailForm()

    return render(request, 'gmail/contact.html', {'form': form})
