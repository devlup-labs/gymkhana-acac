from django.views.generic.base import ContextMixin
from .models import Board, Senate


class NavigationMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(NavigationMixin, self).get_context_data(**kwargs)
        boards = Board.objects.filter(is_active=True)
        senate = Senate.objects.filter(is_active=True).order_by('-year').first()
        context['board_link_list'] = boards
        context['senate'] = senate
        return context
