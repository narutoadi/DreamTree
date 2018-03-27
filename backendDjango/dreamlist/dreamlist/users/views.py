from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User

from rest_framework import generics
from .serializers import UserDetailSerializer

#class UserDetailView(LoginRequiredMixin, DetailView):
class UserDetailView(generics.RetrieveAPIView):
    lookup_field = 'username'
    serializer_class = UserDetailSerializer
    # These next two lines tell the view to index lookups by username
    #slug_field = 'username'
    #slug_url_kwarg = 'username'
    def get_queryset(self):
        return User.objects.all()

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


#class UserListView(LoginRequiredMixin, ListView):
class UserListView(generics.ListAPIView):
    #model = User
    serializer_class = UserDetailSerializer
    # These next two lines tell the view to index lookups by username
    #slug_field = 'username'
    #slug_url_kwarg = 'username'
    def get_queryset(self):
        return User.objects.all()
