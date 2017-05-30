from django.conf.urls import url
from website.views.views import *
from website.views.product_details_view import *
from website.views.category_list_view import *
from website.views.single_category import *
from website.views.shopping_cart_view import *

app_name = "website"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_user, name='login'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^sell$', sell_product, name='sell'),
    url(r'^products$', list_products, name='list_products'),
    url(r'^categories$', category_list, name='categories'),
    url(r'^product_detail/(?P<product_id>.+?)/$', product_detail, name='product_detail'),
    url(r'^addtocart$', add_to_cart, name='add_to_cart'),
    url(r'^paymenttype$', add_payment_type, name='payment_type'),
    url(r'^paymentlist$', all_payment_types, name='paymentlist'),
    url(r'^single_category/(?P<category_id>.+?)/$', single_category, name='single_category'),
    url(r'^shopping_cart$', shopping_cart, name='shopping_cart'),
]
