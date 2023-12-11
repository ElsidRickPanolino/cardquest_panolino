from django.contrib import admin

# Register your models here.
from .models import PokemonCard, Trainer, Collection

# admin.site.register(PokemonCard)

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)
    
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name",)
    
@admin.register(Collection)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("card", "tr", "collection_date")
    search_fields = ("tr",)
    

# admin.site.register(PokemonCard, PokemonAdmin)