from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from catalogue.models import Catalog


class CatalogTestCase(unittest.TestCase):
    def setUp(self):
        Catalog.objects.create(name="LEVELONE", parent=None)
        Catalog.objects.create(name="LEVELTWO", parent="LEVELONE")
        Catalog.objects.create(name="LEVELTHREE", parent="LEVELONE")
        Catalog.objects.create(name="LEVELFOUR", parent="LEVELTWO")
        Catalog.objects.create(name="ONELEVEL", parent=None)
        Catalog.objects.create(name="TWOLEVEL", parent="ONELEVEL")
        Catalog.objects.create(name="THREELEVEL", parent="ONELEVEL")
        Catalog.objects.create(name="FOURLEVEL", parent="TWOLEVEL")

    def display_the_catalogue(self):
        """display the trees below in different ways"""
        onelvl = Catalog.objects.get(name="ONELEVEL")
        lvlone = Catalog.objects.get(name="LEVELONE")
        self.assertEqual(lvlone.get_children, onelvl.get_descendants)
        self.assertEqual(range(10), onelvl.get_descendants)
        self.assertEqual(lvlone.get_children, range(10))