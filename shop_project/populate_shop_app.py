import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','shop_project.settings')
import django
django.setup()


import random
from faker import Faker
from shop_app.models import Client, Product

fakegen = Faker()

def generate_brand():
	brands = ['Nike','Adidas','Rebook','Jordan','Balanciaga','Timberland','School','Tatan','Asics','Geox']
	index = random.randint(0,9)
	return brands[index]

def generate_client():
	for customer in range(1000):
		customer = Client.objects.get_or_create(first_name=fakegen.first_name(),last_name=fakegen.last_name(),email=fakegen.email(),password=fakegen.password())[0]
		
		print(customer)


def generate_product():
	for product in range(50):
		price = random.randint(30, 150)
		brand = generate_brand()
		product = Product.objects.get_or_create(name=brand,price=price,description=fakegen.text(max_nb_chars=100))[0]
		print(product)

def populate():
	generate_product()

if __name__ == '__main__': 
	print('news_client script...') 
	populate()
	print('done populating.')
