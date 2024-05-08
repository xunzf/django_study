from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):
    def process_request(self, request):
        print("request coming")

    def process_response(self, request, response):
        print("response coming")
        return response
