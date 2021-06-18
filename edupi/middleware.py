from datetime import datetime
from cntapp.models import Directory, Document
import re
import os

class ProcessViewNoneMiddleware:
    """
    Provides full logging of requests and responses
    """
    _initial_http_body = None
    print("###############################ProcessViewNoneMiddleware#########################################")

    def __call__(self, request):
        print("callllllllllllll")

    def process_view(request, view_func, *args, **kwargs):
        """url After matching, call before view function call"""
        print("-----process_view-----")

    def process_request(self, request):
        print(request.path_info)
        print("****************")
        # self._initial_http_body = request.body  # this requires because for some reasons there is no way to access request.body in the 'process_response' method.
        if re.match('^(.*/media/).[^/]*.(jpg|png|pdf|apk|mp4|jpeg|svg)$', str(request.path_info)):
            print("save to file")
            BASE_DIR = os.path.dirname(os.path.dirname(__file__))
            log_file = os.path.join(BASE_DIR, '../database/logs.txt')
            file_name = str(request.path_info).split("/media/")[1]
            print(file_name)
            queryset = Document.objects.filter(file="./" + file_name)
            # serializer_class = DocumentSerializer
            for q in queryset:
                print(q.__dict__)
                with open(log_file, "a") as a_file:
                    a_file.write("\n")
                    a_file.write(q.name)
                    a_file.write("\n")
                    a_file.write(q.type)

            # queryset = Document.objects.get(name=file_name)
            # print(queryset)
        else:
            print("don't save")
        print(request.path)
        print("****************")

    def process_response(self, request, response):
        """
        Adding request and response logging
        """

        # queryset = Document.objects.filter(name="")
        # serializer_class = DocumentSerializer
        # for q in queryset:
        #    print(q.__dict__)
        # serializer = serializer_class(queryset)
        # docs = DocumentSerializer(queryset, many=True)

        # print(docs.data)

        print(request.build_absolute_uri())
        print("++++++++++++++++++")
        # print(response.__dict__)
        if type(response._closable_objects) == list and len(response._closable_objects) > 0:
            x = str(response._closable_objects[0]).split("'")[1]
            print(x)
            if re.match('^(.*/media/).[^/]*.(jpg|png|pdf|apk|mp4)$', x):

                print("save to file")
                print(response._closable_objects[0])
            else:
                print("not save")
                print(response._closable_objects[0])


        return response
