from datetime import datetime
from cntapp.models import Directory, Document
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import logging
import re
import os
class ProcessViewNoneMiddleware:
    _initial_http_body = None
    def process_request(self, request):
        if re.match('^(.*/media/).[^/]*.(jpg|png|pdf|apk|mp4|jpeg|svg|pptx|m4v|ppt|doc|docx|xlsx|wmv|mp3)$', str(request.path_info)):
            BASE_DIR = os.path.dirname(os.path.dirname(__file__))
            log_file = os.path.join(BASE_DIR, '../database/logs.txt')
            file_name = str(request.path_info).split('/media/')[1]
            queryset = Document.objects.filter(file='./' + file_name)
            for q in queryset:
                with open(log_file, 'a') as a_file:
                    a_file.write('\n')
                with open(log_file, "a") as a_file:
                    a_file.write("\n")
                    try:
                        a_file.write(str(q.name.encode('utf-8')) + "----" + q.type)
                    except Exception as ex:
                        a_file.write(str(q.name.encode('utf-8', 'surrogateescape')) + "----" + q.type)
                    a_file.write("\n")
                    a_file.write(q.type)
            render_url = "/edupimedia/" + str(file_name)
            logging.warning(render_url)
            return HttpResponseRedirect(render_url)
        elif re.match('^(.*/media/thumbnails).[^/]*.(jpg|png|pdf|apk|mp4|jpeg|svg)$', str(request.path_info)):
            file_name = str(request.path_info).split("/media/")[1]
            render_url = "/edupimedia/" + str(file_name)
            logging.warning(render_url)
            return HttpResponseRedirect(render_url)
        else:
            pass
