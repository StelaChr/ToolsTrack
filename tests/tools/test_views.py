from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from category.models import Category
from tools.models import Tool, Borrow

User = get_user_model()

class ToolCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='tester@example.com',  # add this
            password='testpass'
        )
        self.category = Category.objects.create(owner=self.user, name='Power Tools')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('create-tool'))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f"/accounts/login/?next={reverse('create-tool')}")

    def test_create_tool_logged_in_without_borrow(self):
        login_successful = self.client.login(email='tester@example.com', password='testpass')
        self.assertTrue(login_successful)

        response = self.client.post(reverse('create-tool'), {
            'name': 'Screwdriver',
            'inventory_number': 'INV123',
            'section_number': 'S3',
            'category': self.category.id,
            # No 'is_borrowed' field here, so no borrow form expected
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tool.objects.count(), 1)
        tool = Tool.objects.first()
        self.assertFalse(tool.is_borrowed)
        self.assertEqual(Borrow.objects.count(), 0)

    def test_create_tool_with_borrow(self):
        self.client.login(email='tester@example.com', password='testpass')

        today_str = timezone.now().date().isoformat()  # 'YYYY-MM-DD'

        post_data = {
            'name': 'Hammer',
            'inventory_number': 'INV456',
            'section_number': 'S5',
            'category': self.category.id,
            'is_borrowed': 'on',  # triggers borrow form processing

            # Borrow form fields:
            'borrower_name': 'John Doe',
            'borrower_contact': 'john@example.com',
            'borrowed_at': today_str,
            'returned_at': '',  # can be empty or valid date after borrowed_at
        }

        response = self.client.post(reverse('create-tool'), post_data)

        self.assertEqual(response.status_code, 302)  # success redirect

        tool = Tool.objects.filter(name='Hammer', owner=self.user).first()
        self.assertIsNotNone(tool)

        borrow = Borrow.objects.filter(tool=tool, borrower_name='John Doe').first()
        self.assertIsNotNone(borrow)
