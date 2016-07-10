from rest_framework.test import APITestCase


class IPLogRESTTest(APITestCase):
    '''Tests for ip_log REST service'''
    def test_empty(self):
        '''Ensure that GET returns empty list if there was no POST requests'''
        response = self.client.get('/ip')
        self.assertEqual(response.data, [])

    def test_structure(self):
        '''Ensure that GET returns a list containing one element after
        one POST request. Ensure that element structure is
        {'ip': ..., 'request_dt': ...}
        '''
        self.client.post('/ip')
        response = self.client.get('/ip')
        
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]), 2)
        self.assertIn('ip', response.data[0])
        self.assertIn('request_dt', response.data[0])

    def test_ordering(self):
        '''Ensure that GET returns a list containing two elements after
        two POST requests. Ensure that timestamp in first element is greater
        then timestamp in second element
        '''
        self.client.post('/ip')
        self.client.post('/ip')
        response = self.client.get('/ip')
        
        self.assertEqual(len(response.data), 2)
        self.assertGreater(response.data[0]['request_dt'],
                           response.data[1]['request_dt'])
