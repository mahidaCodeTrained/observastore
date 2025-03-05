from django.test import TestCase
from.models import AboutPage
from django.utils import timezone
from time import sleep

# Create your tests here.


class AboutPageModelTest(TestCase):

    def setUp(self):
        self.about_page = AboutPage.objects.create(
            title="About Us",
            mission="Our mission is to inspire curiosity and discovery of the cosmos.",
            history="Founded in 2025, we have been providing high-quality astronomy equipment.",
            why_shop_here="Shop with us for the best prices and quality.",
            updated_on=timezone.now()
        )
    
    def test_about_page_works(self):
        self.assertEqual(self.about_page.title, "About Us")
        self.assertEqual(self.about_page.mission, "Our mission is to inspire curiosity and discovery of the cosmos.")
        self.assertEqual(self.about_page.history, "Founded in 2025, we have been providing high-quality astronomy equipment.")
        self.assertEqual(self.about_page.why_shop_here, "Shop with us for the best prices and quality.")

    def test_about_page_updated_on(self):
        """Test if the 'updated_on' field is being updated automatically"""
        # Get the current timestamp without microseconds
        initial_updated_on = self.about_page.updated_on.replace(microsecond=0)
        
        # importing sleep from time to test the updated on because it happens automatically at an instant so sleep(1) will allow me to check it
        sleep(1)  # Sleep for 1 second therefore I can ensure that there is a time difference to test it works
        self.about_page.save()
        updated_on = self.about_page.updated_on.replace(microsecond=0)
        self.assertGreater(updated_on, initial_updated_on)

    def test_empty_mission_field(self):
        """Im testing if a mission field can be left empty"""
        about_page = AboutPage.objects.create(
            title="New About Page",
            mission="",  # Empty mission
            history="We just started.",
            why_shop_here="Best deals.",
        )
        self.assertEqual(about_page.mission, "")

    def test_about_page_fields(self):
        """Testing that all the fields that have been said and that should be there on the model are there."""
        fields = [f.name for f in AboutPage._meta.get_fields()]
        expected_fields = ['id', 'title', 'mission', 'history', 'why_shop_here', 'updated_on']
        self.assertTrue(all(field in fields for field in expected_fields))



