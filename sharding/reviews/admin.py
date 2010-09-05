from django.contrib import admin

from reviews import models

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["created", "author_id", "product_id", "rating"]
    list_filter = ["product_id", "author_id", "rating"]
    ordering = ["-created"]
    readonly_fields = ["created"]

    #def queryset(self, request):
    #    return super(ReviewAdmin, self).queryset(request).using(self._using)

admin.site.register(models.Review, ReviewAdmin)

