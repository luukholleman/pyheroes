# Create your views here.
from django.views.generic.base import TemplateView
from hero.models import Hero
from ranklist.models import Ranklist, Category


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        c = super(HomeTemplateView, self).get_context_data()


        categories = Category.objects.order_by('sequence')

        c['categories'] = ()
        # loop categories to get their ranklists and merge it in the tuple
        for category in categories:
            c['categories'] += (
                (category, category.ranklist_set.order_by('name')),
            )

        c['ranklists'] = Ranklist.objects.order_by('category__name')

        c['softcore'] = Hero.objects.filter(hardcore=False)

        c['hardcore'] = Hero.objects.filter(hardcore=True)

        return c