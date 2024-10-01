from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from pytils.templatetags.pytils_translit import slugify

from catalog.models import Product


# Создавайте свои мнения здесь.


class HomePageView(TemplateView):
    template_name = "catalog/home.html"


class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "purchase_price")
    success_url = reverse_lazy("catalog:catalog_list")

    def form_valid(self, form):
        if form.is_valid():
            catalog = form.save()
            catalog.slug = slugify(catalog.title)
            catalog.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "purchase_price")
    success_url = reverse_lazy("catalog:catalog_list")

    def get_success_url(self):
        return reverse('catalog:catalog_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog_list")

