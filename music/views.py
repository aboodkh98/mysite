from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class IndexViwe(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class SongViwe(generic.ListView):
    template_name = 'music/song.html'
    context_object_name = 'Songs'

    def get_queryset(self):
        return Song.objects.all()


class DetailViwe(generic.DetailView):
    template_name = 'music/detail.html'
    model = Album


class CreateAlbum(CreateView):
    template_name = 'music/album_form.html'
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', ]


class CreateSong(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', ]


class UpdateAlbum(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', ]


class UpdateSong(UpdateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', ]


class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('index')


class DeleteSong(DeleteView):
    model = Song
    success_url = reverse_lazy('music:song')


