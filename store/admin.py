from django.contrib import admin
from .models import Product,Variation,ReviewRating

# Register your models here.
# slug url 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
    
class VariationAdmin(admin.ModelAdmin):
    list_display  = ('product','variation_category','variation_value','is_active')
    list_editable = ("is_active",) 
    list_filter   = ('product','variation_category','variation_value')

admin.site.register(Product,ProductAdmin)

# choice for products 
admin.site.register(Variation,VariationAdmin)

# rating model
admin.site.register(ReviewRating)
