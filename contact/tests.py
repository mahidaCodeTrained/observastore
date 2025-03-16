from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .forms import ContactRequestForm
from .models import ContactRequest

class ContactViewTest(TestCase):

    def test_contact_view_get(self):
        """Test GET request to the contact page"""
        response = self.client.get(reverse('contact_form'))
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check that the form is in the context
        self.assertIsInstance(response.context['form'], ContactRequestForm)

    def test_contact_view_post_valid_form(self):
        """Test POST request to the contact page with a valid form"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'store_good': None,  # Optional field
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact_form'), data)
        
        # Check that the response is a redirect after form submission
        self.assertRedirects(response, reverse('contact_form'))
        
        # Check that the success message is present
        storage = get_messages(response.wsgi_request)
        message = list(storage)[0]
        self.assertEqual(str(message), 'Thank you for contacting us! We will look over your contact request and get back to you!')

        # Check that the ContactRequest has been saved in the database
        self.assertEqual(ContactRequest.objects.count(), 1)

    def test_contact_view_post_invalid_form(self):
        """Test POST request to the contact page with an invalid form"""
        data = {
            'name': '',  # Invalid because name is required
            'email': 'invalid-email',  # Invalid email
            'store_good': None,
            'message': ''
        }
        response = self.client.post(reverse('contact_form'), data)
        
        # Check that the response is a 200 status code (form errors should show on the same page)
        self.assertEqual(response.status_code, 200)

        # Check that the form is still in context and has errors
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')
