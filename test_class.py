import pytest
from challenge import Restaurant,CoffeeStore

#invoke using pytest .

def test_restaurant_init():
    r=Restaurant("Test Restaurant","Test Type","Test Street")
    assert isinstance(r,Restaurant)==1

def test_restaurant_served_count():
    r=Restaurant("Test Restaurant","Test Type","Test Street")
    r.set_number_people_served(100)
    r.set_number_people_served(200)
    assert r.number_people_served==300

def test_coffee_class():
    cafe=CoffeeStore("The espresso","GFH Street, KFC","coffee_store")
    cafe.set_number_people_served(300)
    cafe.print_coffe_store_info()
    cafe.print_restaurant_info()
    cafe.print_number_people_served()
    assert isinstance(cafe,CoffeeStore)