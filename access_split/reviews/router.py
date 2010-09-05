class ReviewRouter(object):
    """
    Sends all review-related operations to a database with the alias of
    "reviews" or "reviews-s". No other apps should use this db alias.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "reviews":
            return "reviews-s"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "reviews":
            return "reviews"
        return None

    def allow_syncdb(self, db, model):
        this_app = (model._meta.app_label == "reviews")
        reviews_db = (db in ("reviews", "reviews-s"))
        if this_app:
            return reviews_db
        if reviews_db:
            return False
        return None

