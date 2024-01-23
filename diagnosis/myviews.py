from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth
from django.conf import settings

from .helpers import isHighQuality, retinopathyPresent, severityLevel


# Create your views here.

class DiagnosisView(View):
    def get(self, request):
        return render(request, 'diagnosis/index.html')

    def post(self, request):
        # UPLOAD FUNDUS IMAGE
        # CHECK QUALITY
        # DETECT RETINOPATHY
        # DETERMINE SEVERITY

        img = request.POST['img']
        result = None

        if isHighQuality(img):
            if retinopathyPresent(img):
                result = severityLevel(img)
                return render(request, 'diagnosis/result.html', )
            else:
                result = 'Retinopathy absent'
                messages.success(request, result)
                return render(request, 'diagnosis/index.html')
        else:
            result = 'Image quality too low'
            messages.error(request, result)
            return render(request, 'diagnosis/index.html')
    