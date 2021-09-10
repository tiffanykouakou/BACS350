from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hulk.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page',
            'body': 'Once upon a time ... ',
        }


class WonderWomanView(TemplateView):
    template_name = 'wonder_woman.html'

class SpiderManView(TemplateView):
    template_name = 'spider_man.html'

class HomeView(TemplateView):
    template_name = 'Home.html'

