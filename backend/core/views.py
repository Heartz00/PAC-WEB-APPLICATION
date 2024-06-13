# Create your views here.
from django.shortcuts import render
from .models import Patient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DICOMImage
from .serializers import DICOMImageSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            # Implement your authentication logic here
            # Example:
            if username == 'example' and password == 'password':
                token, _ = Token.objects.get_or_create(user=username)
                return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class DashboardStatsView(APIView):
    def get(self, request):
        # Fetch and calculate dashboard statistics
        stats = {
            'totalPatients': 100,  # Replace with actual data
            'recentActivity': 'Recent activity details',
            'alerts': 5
        }
        return Response(stats, status=status.HTTP_200_OK)


class PatientRecordsView(APIView):
    def get(self, request):
        # Implement logic to fetch patient records
        # Example:
        patients = [
            {'id': 1, 'name': 'John Doe', 'admissionDate': '2024-06-12'},
            {'id': 2, 'name': 'Jane Smith', 'admissionDate': '2024-06-10'},
            # Add more patient records
        ]
        return Response(patients, status=status.HTTP_200_OK)




def api_example(request):
    data = {
        "message": "Hello from Django!"
    }
    return JsonResponse(data)

def home(request):
    return render(request, 'home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patient_list.html', {'patients': patients})


class DICOMImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = DICOMImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_weasis_url(request, dicom_id):
    dicom_image = DICOMImage.objects.get(id=dicom_id)
    file_url = request.build_absolute_uri(dicom_image.file.url)
    
    weasis_url = f"weasis://?requestType=WADO&contentType=application/dicom&objectUID={file_url}"
    return JsonResponse({"weasis_url": weasis_url})