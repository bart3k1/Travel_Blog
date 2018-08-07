from django.contrib.auth.models import User
from django.test import TestCase

from trvl_app.forms import AddUserForm


class LoginPageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_index_page_status_code(self):
        response = self.client.get('/index')
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

    def test_form_bad_email(self):
        form_data = {'username': 'bob', 'password': 'test123', 'password_c': 'test', 'first_name': 'bobi', 'last_name': 'bobber', 'email': 'bobbob.pl'  }
        form = AddUserForm(data=form_data)
        self.assertFalse(form.is_valid())


# class CityFormTest(TestCase):
#
#     def test_form_ok(self):
#         form_data = {'name': 'London', 'date': '2018-08-07 15:00:00'}
#         form = CityForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_form_no_name(self):
#         form_data = {'name': '', 'date': '2018-08-07 15:00:00'}
#         form = CityForm(data=form_data)
#         self.assertFalse(form.is_valid())
