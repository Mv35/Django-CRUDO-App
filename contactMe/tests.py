from django.test import TestCase
from django.http import HttpRequest
from . forms import ContactForm


class TestContactForm(TestCase):
    def test_empty_form(self):
        form = ContactForm()
        self.assertIn("name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("category", form.fields)
        self.assertIn("subject", form.fields)
        self.assertIn("body", form.fields)
    
    def test_simple_form(self):
        request = HttpRequest()
        request.POST = {
            "name": "test",
            "email": "rumbamama@live.com",
            "category": "Question",
            "subject": "testing",
            "body": "hi, this is a unit test"
        }
        form = ContactForm(request.POST)
        self.assertTrue(form.fields.get(key) for key in form.fields)