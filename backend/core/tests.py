from django.test import TestCase
from .models import Patient
from datetime import date  # Import the date class

class PatientTestCase(TestCase):
    def setUp(self):
        # Provide a date_of_birth value
        Patient.objects.create(
            first_name="John",
            last_name="Doe",
            medical_record_number="12345",
            date_of_birth=date(1990, 1, 1)  # Set a valid date
        )

    def test_patient_name(self):
        john = Patient.objects.get(medical_record_number="12345")
        self.assertEqual(john.first_name, "John")
