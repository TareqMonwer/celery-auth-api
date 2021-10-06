from django.shortcuts import render


def list_urls(request):
    urls = [{'name': 'signup', 'link': 'accounts/signup'},
            {'name': 'login', 'link': 'accounts/login'}]
    return render(request, 'core/links.html', {'urls': urls})
