from django.contrib import admin
from cars.models import Cars, CarSeries, CarSeriesComments, CarForms
from django.utils.safestring import mark_safe
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from import_export.admin import ImportExportModelAdmin
from cars.resources import CarsResource
# Register your models here.

class CommentInline(admin.TabularInline):
    model = CarSeriesComments
    fields = ('comment', 'active',)
    extra = 0
    classes = ('collapse',)

    

class CarsAdmin(admin.ModelAdmin):
    list_display = ( 'manufacturer', 'published_date',)
    readonly_fields = ('published_date', 'updated_date',)
    search_fields = ('manufacturer',)
    prepopulated_fields = {'slug':('manufacturer',)}
    list_per_page = 10
    ordering = ('manufacturer',)
    fields = ('manufacturer','slug','description','published_date','updated_date',)

    


class CarsSeriesAdmin(ImportExportModelAdmin):
    list_display = ('model','serie','year','active','how_many_comments','list_get_image',)
    list_filter = (
            ('model', RelatedDropdownFilter),
            #('serie', RelatedDropdownFilter),
            #('year', RelatedDropdownFilter),
        )
    # list_editable = ('active',)
    ordering = ('year',)
    search_fields = ('model__manufacturer','serie','year',)
    actions = ('activate_action','deactivate_action',)
    list_per_page = 10
    readonly_fields = ('image_of_car',)
    fieldsets = (
        ('Main',{
            'fields':('model','serie','modelnumber','type','year','active',),
            'description': 'Main configurations'
        }),
        ('Image Settings',{
            'fields':('image','image_of_car'),
            'description':'Image configurations'
        })

    )
    filter_horizontal = ('type',)
    inlines = (CommentInline,)
    resource_class = CarsResource

    #def has_delete_permission(self, request, obj=None):  ### Default olaraq modele gore silme islemini legv etmek ucun 
      #  return False

    def activate_action(self, request, queryset):
        count = queryset.update(active=True)
        self.message_user(request, f'{count} object activated ')
    
    def deactivate_action(self, request, queryset):
        count = queryset.update(active=False)
        self.message_user(request, f'{count} object deactivated ')
    
    activate_action.short_description = 'Activate object'
    deactivate_action.short_description = 'Deactivate object'
    
    
    def list_get_image(self,obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=55 height=40></img>")
        return mark_safe("NO IMAGE")
    list_get_image.short_description = 'Image of car'


class CarsSeriesCommentsAdmin(admin.ModelAdmin):
    list_display = ('__str__','add_date','active',)
    search_fields = ('modelnumbers__model__manufacturer','modelnumbers__modelnumber','modelnumbers__serie',)
    list_filter = ('add_date',)                                              
    ordering = ('add_date',)
    readonly_fields = ('add_date',)
    list_per_page = 11
    list_editable = ('active',)
    raw_id_fields =('modelnumbers',)

    




admin.site.register(Cars, CarsAdmin)
admin.site.register(CarSeries, CarsSeriesAdmin)
admin.site.register(CarSeriesComments,CarsSeriesCommentsAdmin)
admin.site.register(CarForms)