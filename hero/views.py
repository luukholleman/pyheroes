# Create your views here.
from django.views.generic.detail import DetailView
from api.battleapi import call, CAREER_URL, HERO_URL
from hero.models import Hero
from pyheroes import settings


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Hero

    def get_context_data(self, **kwargs):
        c = super(HeroDetailView, self).get_context_data(**kwargs)

        url = CAREER_URL % ('eu', 'Aveley-2218')

        career, last_modified = call(url)
        # career = Career('eu', 'Aveley#2218')

        name = career['battleTag']

        # name = career.battletag

        return c