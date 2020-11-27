from django.contrib import admin
from store.models import Product,Cart,Wishlist,Contact,events,Journal,Donations

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Contact)
admin.site.register(events)
admin.site.register(Journal)
admin.site.register(Donations)