from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
import requests
from . import models, serializers
from omaralbeik import server_variables as sv

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    http_method_names = ["post"]

    def create(self, request):
        serializer = serializers.MessageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            self.validate_recaptcha(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def validate_recaptcha(self, request):
        err_message = 'Unable to verify ReCAPTCHA'
        if 'recaptcha_response' not in request.data:
            raise ValueError(err_message)
        req = requests.post('https://www.google.com/recaptcha/api/siteverify', {
            'secret': sv.RECAPTCHA_SECRET_KEY,
            'response': request.data['recaptcha_response'],
            'remoteip': self.get_client_ip(request)
        })
        if not req.json()['success']:
            raise ValueError(err_message)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
