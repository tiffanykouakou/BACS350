from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hulk.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page',
            'body': 'Once upon a time ... ',
        }


class IronManView(TemplateView):
    template_name = "iron_man.html"

class BlackWidowView(TemplateView):
    template_name = "black_widow.html"
