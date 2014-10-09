# Seed File: Did not want to go with fixtures as 
# edits to data might be required during development

# Create sample users: Note that these are not superusers,
# and they must till be added to customers until controllers automate this
from django.contrib.auth.models import User
from thuzioapp.models import Purchase, Customer, Product
jim = User.objects.create_user('Jim', 'jim@gmail.com', 'password')
jim.save()

jim = Customer(first_name="Jim", last_name="Jones", email_address = "jim@gmail.com", address="jim drive", zipcode=12345, cc_number=1111111111111111, level=1, user_id=2)


paul = User.objects.create_user('Paul', 'paul@gmail.com', 'password')
paul.save()


