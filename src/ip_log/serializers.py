from rest_framework import serializers


class RequestLogSerializer(serializers.Serializer):
    '''Serializer for ip_log.RequestLog model'''    
    ip = serializers.IPAddressField(read_only=True)
    request_dt = serializers.DateTimeField(read_only=True)
