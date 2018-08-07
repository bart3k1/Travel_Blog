from django.contrib.auth.models import User
from django.test import TestCase

from trvl_app.forms import AddUserForm
from trvl_app.models import Travel


class LoginPageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)


class LogInTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'passsss'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_login_bad_pass(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'passsssxxx'}
        response = self.client.post('', self.credentials, follow=True)
        self.assertFalse(response.context['user'].is_active)

    def test_login_bad_user(self):
        self.credentials = {
            'username': 'testuserxxx',
            'password': 'passsss'}
        response = self.client.post('', self.credentials, follow=True)
        self.assertFalse(response.context['user'].is_active)


class AddUserFormTest(TestCase):
    def test_form_no_user(self):
        form_data = {'username': '', 'password': 'test123', 'password_c': 'test123', 'first_name': 'bobi', 'last_name': 'bobber', 'email': 'bob@bob.pl'  }
        form = AddUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_ok(self):
        form_data = {'username': 'bob', 'password': 'test123', 'password_c': 'test123', 'first_name': 'bobi', 'last_name': 'bobber', 'email': 'bob@bob.pl'  }
        form = AddUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_bad_pass_c(self):
        form_data = {'username': 'bob', 'password': 'test123', 'password_c': 'test', 'first_name': 'bobi', 'last_name': 'bobber', 'email': 'bob@bob.pl'  }
        form = AddUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_short_pass(self):
        form_data = {'username': 'bob', 'password': '123', 'password_c': '123', 'first_name': 'bobi', 'last_name': 'bobber', 'email': 'bob@bob.pl'  }
        form = AddUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_bad_email(self):
        form_data = {'username': 'bob', 'password': 'test123', 'password_c': 'test', 'first_name': 'bobi', 'last_name': 'bobber', 'email': 'bobbob.pl'  }
        form = AddUserForm(data=form_data)
        self.assertFalse(form.is_valid())


class AddTravelFormTest(TestCase):

    def test_add_travel_post(self):
        test_user = User.objects.create(username="newuser", password="securetestpassword")
        Travel.objects.create(author=test_user, topic="Super Important Test", content="This is really important.")
        self.assertEqual(Travel.objects.last().topic, "Super Important Test")
