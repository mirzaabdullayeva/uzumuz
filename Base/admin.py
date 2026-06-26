from django.contrib import admin

from .models import *
from .models import Course


admin.site.register(Course)




# Register your models here.
admin.site.register(Item)

admin.site.register(Main_branch)

admin.site.register(Category)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Men)
admin.site.register(Contact)
# server is working 

# 200
# 404
# 500 --- server is not working