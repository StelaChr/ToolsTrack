from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from tools.forms import BorrowForm


class BorrowFormTest(TestCase):

    def test_borrow_form_valid_data(self):
        data = {
            'borrower_name': 'Alice',
            'borrower_contact': 'alice@example.com',
            'borrowed_at': timezone.now().date(),
            'returned_at': timezone.now().date() + timedelta(days=1),
        }
        form = BorrowForm(data=data)
        self.assertTrue(form.is_valid())

    def test_borrow_form_returned_before_borrowed(self):
        data = {
            'borrower_name': 'Bob',
            'borrower_contact': 'bob@example.com',
            'borrowed_at': timezone.now().date(),
            'returned_at': timezone.now().date() - timedelta(days=1),  # invalid
        }
        form = BorrowForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('Return date cannot be before borrow date.', form.errors['__all__'])

    def test_borrow_form_optional_fields_blank(self):
        data = {
            'borrower_name': 'Charlie',
            'borrowed_at': timezone.now().date(),
            'returned_at': '',  # blank is allowed
            'borrower_contact': '',  # blank is allowed
        }
        form = BorrowForm(data=data)
        self.assertTrue(form.is_valid())

    def test_borrow_form_missing_required(self):
        data = {
            'borrower_name': '',
            'borrowed_at': '',
        }
        form = BorrowForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('borrower_name', form.errors)
        self.assertIn('borrowed_at', form.errors)