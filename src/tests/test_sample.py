import os, unittest
from .base import TestWrapper

 
class TestUser(TestWrapper):
 
    ###############
    #### tests ####
    ###############
 
    def test_get_all_users(self):
        response = self.app.get('/user', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
