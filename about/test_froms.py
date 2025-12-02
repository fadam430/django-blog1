from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.

class TestCollaborateForm(TestCase):
    
    def test_from_valid_data(self):
        form = CollaborateForm({
            'name': 'Jhon Doe',
            'email': 'test@test.com',
            'message': 'This is a test message.'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid.")
        
    def test_from_name_empty(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'This is a test message.'
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when name is empty.")
        
    def test_from_email_empty(self):
        form = CollaborateForm({
            'name': 'Jhon Doe',
            'email': '',
            'message': 'This is a test message.'
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when email is empty.")
    
    def test_from_message_empty(self):
        form = CollaborateForm({
            'name': 'Jhon Doe', 
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when message is empty.")
        