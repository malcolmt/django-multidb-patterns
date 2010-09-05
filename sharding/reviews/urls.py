from django.conf.urls.defaults import *     # pylint: disable-msg=W0401,W0614
from django.shortcuts import redirect

from reviews import views

def redirect_to(request, **kwargs):
    return redirect(**kwargs)

urlpatterns = patterns("",
    url("^$", redirect_to, {"to": "product-reviews", "permanent": True}),
    url("review/products/(?:(?P<product_id>\d+)/)?$", views.product_reviews,
            name="product-reviews"),
    url("review/(?:(?P<review_id>\d+)/)?$", views.show_review,
            name="show-review"),
    url("review/create/(?:(?P<product_id>\d+)/)?$", views.add_review,
            name="add-review"),
)

