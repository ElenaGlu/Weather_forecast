from django.shortcuts import render


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, KeyError):
            return render(request, 'App/404.html', status=404)
        elif isinstance(exception, ValueError):
            return render(request, 'App/404.html', status=404)
        else:
            return render(request, 'App/500.html', status=500)
