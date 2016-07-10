from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from ipware.ip import get_ip
from django.conf import settings

from ip_log.models import RequestLog
from ip_log.serializers import RequestLogSerializer


class IPLog(ListAPIView):
    '''ip_log REST service
    
    Two methods implemented:
    POST - stores information about this method call (client IP and
        timestamp). POST method accepts no arguments and returns
        nothing. Responds with 500 Internal Server Error in case
        if client IP can not be resolved
    GET - returns a list of POST method calls ordered by timestamp
        descednding. Information about each call includes client ip and
        timestamp of POST method call. 
    '''    
    queryset = RequestLog.objects.order_by('-request_dt')
    serializer_class = RequestLogSerializer
    
    class IpLogPagination(LimitOffsetPagination):
        '''Pagination settings for GET request. Standard limit-offset
        pagination is used. The maximum number of records that can be
        requested at a time is set to IP_LOG_MAX_LIMIT setting.
        '''
        max_limit = settings.IP_LOG_MAX_LIMIT

    pagination_class = IpLogPagination

    class UnableToResolveIPException(APIException):
        '''This exception is raises by post method when client IP
        can not be resolved
        '''
        default_detail = 'Your IP can not be resolved'
        
    def post(self, request, format=None):
        '''ip_log REST serivice POST method implementation.'''
        client_ip = get_ip(request)
        
        if client_ip == None:
            raise IPLog.UnableToResolveIPException()
                
        RequestLog(ip=client_ip).save()
        
        return Response()
