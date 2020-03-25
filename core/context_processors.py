def info(request):
    from core.models import Page
    return {'page': Page.objects.all()}

def moredata(request):
    from core.models import Links
    return {'links': Links.objects.all()}