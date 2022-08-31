from django.shortcuts import render


def home(request):

    return render(request, 'pages/home.html')


def about(request):

    return render(request, 'pages/about.html')


def contact(request):

    return render(request, 'pages/contact.html')


def handler404(request, exception):

    return render(request, 'error/404.html', {'error': exception}, status=404)


def handler500(request, exception=None):

    return render(request, 'error/500.html', {}, status=500)

    # pass
# on mets passe quand on ne sait pas encore quoi mettre dans notre fonction
