from django.contrib import admin

from reviews import models

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["created", "author_id", "product_id", "rating", "db_num"]
    list_filter = ["product_id", "author_id", "rating"]
    ordering = ["-created"]
    readonly_fields = ["created"]

    def db_num(self, obj):
        return unicode(obj.get_db_num())

    # TODO: Need a custom QuerySet here that chains results from each a base
    # QuerySet run against each db alias in turn.
    #def queryset(self, request):
    #    return super(ReviewAdmin, self).queryset(request).using(self._using)

admin.site.register(models.Review, ReviewAdmin)

