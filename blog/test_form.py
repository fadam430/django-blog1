from django.test import TestCase
from .forms import CommentForm

# Create your tests here.

class TestCommentForm(TestCase):
    
    def test_form_valid_data(self):
        comment_form = CommentForm({'body': 'This is a test comment.'})
        self.assertTrue(comment_form.is_valid(), msg="Form should be valid with correct data.")
        
    def test_form_no_data(self):
        comment_form = CommentForm({})
        self.assertFalse(comment_form.is_valid(), msg="Form should be invalid with no data.")
        