from django.contrib.sites.models import Site

def get_site_name(request):
    site = Site.objects.get_current()

    return {
        'site' : site,
    }
