from django.test import TestCase
from django.contrib.auth import get_user_model
from tools.models import Tool, Borrow
from category.models import Category

User = get_user_model()

class ToolModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='tester@example.com',  # add this
            password='testpass'
        )
        self.category = Category.objects.create(owner=self.user, name='Cutting')
        self.tool = Tool.objects.create(
            name='Hammer',
            owner=self.user,
            category=self.category,
            inventory_number='INV001',
            section_number='S1',
            is_borrowed=True,
        )

    def test_tool_str(self):
        self.assertEqual(str(self.tool), "Hammer (Cutting)")

    def test_tool_fields(self):
        self.assertTrue(self.tool.is_borrowed)
        self.assertEqual(self.tool.inventory_number, 'INV001')

class BorrowModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='tester@example.com',  # add this
            password='testpass'
        )
        self.category = Category.objects.create(owner=self.user, name='Drills')
        self.tool = Tool.objects.create(
            name='Drill',
            owner=self.user,
            category=self.category,
            inventory_number='INV002',
            section_number='S2'
        )

    def test_borrow_str(self):
        borrow = Borrow.objects.create(tool=self.tool, borrower_name="Alice")
        self.assertIn("Alice", str(borrow))