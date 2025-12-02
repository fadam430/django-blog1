from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About, CollaborateRequest


# Create your tests here.

class TestCollaborateForm(TestCase):
    
    def setUp(self):
        self.about_content = About(
            title="About me",
            content="This is some information about me.",
        )
        self.about_content.save()
    
        
    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About me", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
    
    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavor to respond within 2 working days.', response.content)
        
    