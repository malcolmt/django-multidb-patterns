from django.contrib import admin

from reviews import models

class ReviewAdmin(admin.ModelAdmin):
    """
    Minimal admin class for pulling review records from the "reviews" database.
    Since there are no relations in the review model, we don't need to override
    any of the relation methods, just the query and save methods.
    """
    list_display = ["created", "author_id", "product_id", "rating"]
    list_filter = ["product_id", "author_id", "rating"]
    ordering = ["-created"]
    readonly_fields = ["created"]
    _using = "reviews"

    def save_model(self, request, obj, form, change):
        obj.save(using=self._using)

    def queryset(self, request):
        return super(ReviewAdmin, self).queryset(request).using(self._using)

admin.site.register(models.Review, ReviewAdmin)

