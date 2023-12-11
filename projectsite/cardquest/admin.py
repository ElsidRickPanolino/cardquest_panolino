from django.contrib import admin

# Register your models here.
from .models import PokemonCard, Trainer, Collection

# admin.site.register(PokemonCard)

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "hp", "card_type", "attack", "description", "weakness", "card_number", "release_date", "evolution_stage", "abilities")
    search_fields = ("name",)
    
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate","location", "email")
    search_fields = ("name",)
    
@admin.register(Collection)
class  CollectionAdmin(admin.ModelAdmin):
    list_display = ("card", "tr", "collection_date")
    search_fields = ("tr",)
    

# admin.site.register(PokemonCard, PokemonAdmin)