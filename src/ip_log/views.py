from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
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
        if client IP can not be resolved.
    GET - returns a list of POST method calls ordered by timestamp
        descednding. Information about each call includes client ip and
        timestamp. Method accepts standard pagination parameters:
        limit and offset. 
    '''    
    queryset = RequestLog.objects.order_by('-request_dt')
    serializer_class = RequestLogSerializer
    
    class IpLogPagination(LimitOffsetPagination):
        '''Pagination settings for GET request. Standard limit-offset
        pagination is used. Values for default_limit and max_limit are 
        taken from settings. 
        '''
        default_limit = settings.IP_LOG_DEFAULT_LIMIT
        max_limit = settings.IP_LOG_MAX_LIMIT

    pagination_class = IpLogPagination

    def post(self, request, format=None):
        '''ip_log REST serivice POST method implementation.'''
        client_ip = get_ip(request)
        
        if client_ip == None:
            return Response({'error': 'ip_cannot_be_resolved'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        RequestLog(ip=client_ip).save()
        
        return Response()
