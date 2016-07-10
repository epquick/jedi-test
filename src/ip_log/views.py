import logging

from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from django.conf import settings
from ipware.ip import get_ip

from ip_log.models import RequestLog
from ip_log.serializers import RequestLogSerializer


logger = logging.getLogger(__name__)


class IPLog(ListAPIView):
    '''REST service
    
    Two methods implemented:
    POST - stores information about this method call (client IP and
        timestamp). POST method accepts no arguments and returns
        nothing.
        Responds with 500 Internal Server Error if client IP can not be
        resolved, response body will be {'detail': 'ip_cannot_be_resolved'}
        in that case
    GET - returns a list of POST method calls ordered by timestamp
        descednding. Information about each call includes client ip and
        timestamp. Method accepts standard pagination parameters
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
    
    class IPCannotBeResolvedException(APIException):
        '''Exception that throws by post method in case if
        client IP can not be resolved
        '''
        default_detail = 'ip_cannot_be_resolved'    
    
    def get(self, *args, **kwargs):
        '''ip_log REST serivice GET method implementation.'''
        logger.info('IPLog GET method requested')
        return super(IPLog, self).get(*args, **kwargs)

    def post(self, request, format=None):
        '''ip_log REST serivice POST method implementation.'''
        logger.info('IPLog POST method requested')

        client_ip = get_ip(request)
        
        if client_ip == None:
            logger.info('Unable to resolve IP:\n%s' % request.META)
            raise IPLog.IPCannotBeResolvedException
        
        RequestLog(ip=client_ip).save()
        
        return Response()