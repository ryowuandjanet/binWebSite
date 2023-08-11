from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render
from typing import Any, Dict
from django.core.paginator import (
    PageNotAnInteger,
    EmptyPage,
    InvalidPage,
    Paginator
)

from cart.carts import Cart
from .models import (
    Category,
    Product,
    Slider
)

class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context.update(
            {
                'featured_categories': Category.objects.filter(featured = True),
                'featured_products': Product.objects.filter(featured = True),
                'categories': Category.objects.all(),
                'sliders': Slider.objects.filter(show=True)
            }
        )
        return context

class About(generic.TemplateView):
    template_name = 'about.html'


# 三角台曆區
class Tdca(generic.TemplateView):
    template_name = 'pages/triangular_desk_calendar_area.html'

# 中西式桌曆
class Cawsdc(generic.TemplateView):
    template_name = 'pages/Chinese_and_western_style_desk_calendar.html'

# 便條盒區
class Nba(generic.TemplateView):
    template_name = 'pages/note_box_area.html'

# 工商手冊
class Bh(generic.TemplateView):
    template_name = 'pages/business_handbook.html'

# 年曆掛軸
class Chs(generic.TemplateView):
    template_name = 'pages/calendar_hanging_scroll.html'

# 日曆 農民曆區
class Cpcd(generic.TemplateView):
    template_name = 'pages/calendar_peasant_calendar_district.html'

# 月曆區
class Ca(generic.TemplateView):
    template_name = 'pages/calendar_area.html'


class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'product/product-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context

class CategoryDetails(generic.DetailView):
    model = Category
    template_name = 'product/category-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_object().products.all()
        return context

class CustomerPaginator:
    def __init__(self,request,queryset,paginted_by) -> None:
        self.paginator = Paginator(queryset,paginted_by)
        self.paginated_by = paginted_by
        self.queryset = queryset
        self.page = request.GET.get('page',1)
    
    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)
        return queryset

class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        page_obj = CustomerPaginator(self.request, self.get_queryset(),self.paginate_by)
        queryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['object_list'] = queryset
        context['paginator'] = paginator
        return context
    
class SearchProducts(generic.View):
    def get(self, *args, **kwargs):
        key = self.request.GET.get('key',"")
        products=Product.objects.filter(
            Q(title__icontains = key) |
            Q(category__title__icontains = key)
        )
        context = {
            'products': products,
            "key": key
        }
        return render(self.request, 'product/search-products.html',context)