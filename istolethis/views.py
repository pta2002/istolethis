from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from . import forms
from .models import *
from django.db.models import Count, F, Q


def home(request):
    games = Game.objects.annotate(children=Count('gametext'))\
                .filter(Q(children__lt=F('until')) | Q(children__lte=0),
                        over=False)
    return render(request, 'istole/home.html', {'games': games})


def new(request):
    if request.method == "POST":
        form = forms.NewGameForm(request.POST)

        if form.is_valid():
            g = Game(title=form.data['title'], until=form.data['iterations'])
            g.save()

            initText = GameText(game=g, text=form.data['text'])
            initText.save()

            messages.success(request, "Game created!")
            return redirect(reverse('istole:manage',
                                    kwargs={'uuid': g.game_id}))
    else:
        form = forms.NewGameForm()
    return render(request, 'istole/new.html', {'form': form})


def play(request, id):
    game = get_object_or_404(GameText, id=id)
    game = game.game.get_latest()

    if game.game.is_over():
        messages.warning(request, "Game is over!")
        return redirect(reverse('istole:home'))

    if request.method == "POST":
        form = forms.PostTextForm(request.POST)

        if form.is_valid():
            text = GameText(game=game.game, text=form.data['text'])
            text.save()

            messages.success(request, "Submitted!")
            return redirect(reverse('istole:home'))
    else:
        form = forms.PostTextForm()
    return render(request, 'istole/play.html', {'form': form,
                                                'game': game.game})


def manage(request, uuid):
    game = get_object_or_404(Game, game_id=uuid)
    texts = game.gametext_set.order_by('submitted_at')

    return render(request, 'istole/manage.html', {'game': game,
                                                  'texts': texts})


def stop(request, uuid):
    game = get_object_or_404(Game, game_id=uuid)

    game.over = True
    game.save()

    messages.success(request, "Game stopped!")
    return redirect(reverse('istole:manage', kwargs={'uuid': game.game_id}))
