from django.test import TestCase
from.models import AboutPage

# Create your tests here.


class AboutPageModelTest(TestCase):

    def setUp(self):
        self.about_page = AboutPage.objects.create(
            title="About Us",
            mission="Our mission is to inspire curiosity and discovery of the cosmos.",
            history="Founded in 2010, we have been providing high-quality astronomy equipment.",
            why_shop_here="We offer expert advice, high-quality products, and excellent customer service."
        )
    
    def test_about_page_works(self):
        self.assertEqual(self.about_page.title, "About Us")
        self.assertEqual(self.about_page.mission, "This will fail")


