from django.test import TestCase

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Karen = hood(hood='Karen')

    def test_instance(self):
        self.assertTrue(isinstance(self.Karen,hood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Karen.save_hood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Karen.delete_neighbourhood('Karen')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

