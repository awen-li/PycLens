# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_get_dir_redirect_location_domain_injection_bug

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(os.path.join(self.tempdir, 'existing_directory'))
    url = f'/python.org/..%2f..%2f..%2f..%2f..%2f../%0a%0d/../{self.tempdir_name}/existing_directory'
    expected_location = f'{url}/'
    response = self.request(url)
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    location = response.getheader('Location')
    self.assertEqual(location, expected_location, msg='non-attack failed!')
    attack_url = f'/{url}'
    response = self.request(attack_url)
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    location = response.getheader('Location')
    self.assertFalse(location.startswith('//'), msg=location)
    self.assertEqual(location, expected_location, msg='Expected Location header to start with a single / and end with a / as this is a directory redirect.')
    attack3_url = f'//{url}'
    response = self.request(attack3_url)
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    self.assertEqual(response.getheader('Location'), expected_location)
    attack_scheme_netloc_2slash_url = f'https://pypi.org/{url}'
    expected_scheme_netloc_location = f'{attack_scheme_netloc_2slash_url}/'
    response = self.request(attack_scheme_netloc_2slash_url)
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    location = response.getheader('Location')
    self.assertTrue(location.startswith('https://pypi.org/'), msg=location)
