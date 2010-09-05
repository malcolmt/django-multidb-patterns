from django.contrib import admin
from django.contrib.admin import actions

from reviews import models

class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for pulling review records from the "reviews" database. Since
    there are no relations in the review model, we don't need to override any
    of the relation methods, just the query and save methods.

    Most of the excitement here is in providing a sensible "delete" method for
    a setup that doesn't have database replication (see get_actions() and
    delete_from_dbs()).
    """
    list_display = ["created", "author_id", "product_id", "rating",
            "in_shadow_db"]
    list_filter = ["product_id", "author_id", "rating"]
    ordering = ["-created"]
    readonly_fields = ["created"]
    actions = ["copy_to_shadow", "delete_from_dbs"]
    _using = "reviews"

    # Our delete_from_dbs action uses default delete_selected action code, so
    # we set the right template to use for that action.
    delete_selected_confirmation_template = "reviews/delete_from_db.html"

    def save_model(self, request, obj, form, change):
        obj.save(using=self._using)

    def queryset(self, request):
        return super(ReviewAdmin, self).queryset(request).using(self._using)

    def get_actions(self, request):
        """
        Hackity-hack-hack: A small modification on the default get_actions()
        that removes the delete_selected action, since it doesn't work for our
        situation. Django should make this easier, but, as of 1.2, this code
        necessary.
        """
        actions = super(ReviewAdmin, self).get_actions(request)
        del actions["delete_selected"]
        return actions

    # XXX Ideally, I'd like to override delete_selected, but that seems
    # fragile (relies on sorting order of descriptions as to who wins), so
    # let's just create a separate action.
    def delete_from_dbs(self, request, queryset):
        """
        Delete requested records from both databases.
        """
        result = actions.delete_selected(self, request, queryset)
        if request.POST.get("post"):
            # The master copies (default write db for the model) have already
            # been deleted. We need to nuke the shadow copies.
            queryset.using("reviews-s").delete()
        return result

    def copy_to_shadow(self, request, queryset):
        """
        Copies various reviews to the shadow database.
        """
        for review in queryset:
            review.save(using="reviews-s")


admin.site.register(models.Review, ReviewAdmin)

