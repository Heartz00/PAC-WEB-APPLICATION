from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    medical_record_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Image(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='images/')
    modality = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.modality} for {self.patient}"
    
class DICOMImage(models.Model):
    file = models.FileField(upload_to='dicom_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    report_file = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.patient} on {self.created_at}"
