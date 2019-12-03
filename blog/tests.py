from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import post_list,post_detail,post_new,post_edit,inicio

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_inicio_resolves(self):
        url=reverse('inicio')
        self.assertEquals(resolve(url).func,inicio)

    def test_post_list_resolves(self):
        url=reverse('post_list') 
        self.assertEquals(resolve(url).func,post_list)
        
    def test_post_detail_resolves(self):
        url=reverse('post_detail') 
        self.assertEquals(resolve(url).func,post_detail)

    def test_post_new_resolves(self):
        url=reverse('post_new') 
        self.assertEquals(resolve(url).func,post_new)

    def test_post_edit_resolved(self):
        url=reverse('post_edit') 
        self.assertEquals(resolve(url).func,post_edit)