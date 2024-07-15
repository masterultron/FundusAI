from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Diagnosis
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
from .forms import DiagnosisForm
from .models import Diagnosis

# from .helpers import isHighQualityImage, isRetinopathyPresent, severityLevel, get_x, get_y, get_features, get_output
from .helpers import isHighQualityImage, isRetinopathyPresent, severityLevel
from django.core.files.uploadedfile import InMemoryUploadedFile
import tempfile
import os



def get_x(r): 
    return image_path/r['train_image_name']

def get_y(r): 
    return r['class']

def get_features(r): return image_path/r['image']

def get_output(r): return r['quality']


def diagnosis(request):
    return render(request, 'diagnosis/diagnosis.html')


@csrf_exempt
def check_image_quality(request):
    if request.method == 'POST':
        # Assuming the image is sent as 'image' in the POST data

        # Get the uploaded image
        uploaded_image = request.FILES.get('image')

        if uploaded_image and isinstance(uploaded_image, InMemoryUploadedFile):
            # Create a temporary file and write the content of the uploaded image
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                temp_file.write(uploaded_image.read())

            # Now, temp_file.name contains the path to the temporary file
            print(temp_file.name)

            # You can use temp_file.name in your processing logic or return it in the response
            # For example:
            result = isHighQualityImage(temp_file.name)

            # Delete the temporary file after using it
            os.remove(temp_file.name)
            
            if result:
                return JsonResponse({"is_high_quality": True})
            else:
                return JsonResponse({"is_high_quality": False})

        else:
            return JsonResponse({'error': 'No valid image uploaded'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def is_retinopathy_present(request):
    if request.method == 'POST':
        # Assuming the image is sent as 'image' in the POST data
        uploaded_image = request.FILES.get('image')

        if uploaded_image:
            # Assuming you have an is_retinopathy_present function in your helpers
            retinopathy_result = isRetinopathyPresent(uploaded_image)
            pred_output = retinopathy_result[0]
            recommendation = retinopathy_result[1]
            return JsonResponse({
                'is_retinopathy_present': pred_output,
                'recommendation': recommendation
                })

    else:
        # TO-DO: proper error handling
        return JsonResponse({'is_retinopathy_present': False})


@csrf_exempt
def severity_level(request):
    if request.method == 'POST':
        # Assuming the image is sent as 'image' in the POST data
        uploaded_image = request.FILES.get('image')

        if uploaded_image:
            # Assuming you have a severityLevel function in your helpers
            result = severityLevel(uploaded_image)
            return JsonResponse({'result': result})

    return JsonResponse({'result': 'Error'})


def old_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST, request.FILES)
        if form.is_valid():                    
            diagnosis_instance = form.save(commit=False)

            if isHighQualityImage(diagnosis_instance.image, True):
                if isRetinopathyPresent(diagnosis_instance.image, True):
                    diagnosis_instance.result = severityLevel(diagnosis_instance.image)
                    diagnosis_instance.save()
                    return redirect('result', pk=diagnosis_instance.pk)
                else:
                    diagnosis_instance.result = 'Retinopathy absent'
                    diagnosis_instance.save()
                    messages.success(request, diagnosis_instance.result)
            else:
                diagnosis_instance.result = 'Image quality too low'
                diagnosis_instance.save()
                messages.error(request, diagnosis_instance.result)
    else:
        form = DiagnosisForm()

    return render(request, 'diagnosis/diagnosis.html', {'form': form})

def result(request, pk):
    diagnosis_instance = get_object_or_404(Diagnosis, pk=pk)
    return render(request, 'diagnosis/result.html', {'diagnosis_instance': diagnosis_instance})
