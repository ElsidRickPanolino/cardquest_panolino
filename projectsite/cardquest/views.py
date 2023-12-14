from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.models import PokemonCard, Trainer
from cardquest.forms import TrainerForm, PokemonCardForm

from django.urls import reverse_lazy

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15
    
class PokemonList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon'
    template_name = 'pokemon-card.html'
    paginate_by = 15
    
    
class CollectionList(ListView):
    model = PokemonCard
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 15
    
    
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')
    
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')
    
    
class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')
    
    
class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_add.html'
    success_url = reverse_lazy('pokemon-list')
    
class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_edit.html'
    success_url = reverse_lazy('pokemon-list')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemon_del.html'
    success_url = reverse_lazy('pokemon-list')