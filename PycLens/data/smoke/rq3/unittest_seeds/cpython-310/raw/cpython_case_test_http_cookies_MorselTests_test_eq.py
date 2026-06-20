# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base_case = ('key', 'value', '"value"')
    attribs = {'path': '/', 'comment': 'foo', 'domain': 'example.com', 'version': 2}
    morsel_a = cookies.Morsel()
    morsel_a.update(attribs)
    morsel_a.set(*base_case)
    morsel_b = cookies.Morsel()
    morsel_b.update(attribs)
    morsel_b.set(*base_case)
    self.assertTrue(morsel_a == morsel_b)
    self.assertFalse(morsel_a != morsel_b)
    cases = (('key', 'value', 'mismatch'), ('key', 'mismatch', '"value"'), ('mismatch', 'value', '"value"'))
    for case_b in cases:
        with self.subTest(case_b):
            morsel_b = cookies.Morsel()
            morsel_b.update(attribs)
            morsel_b.set(*case_b)
            self.assertFalse(morsel_a == morsel_b)
            self.assertTrue(morsel_a != morsel_b)
    morsel_b = cookies.Morsel()
    morsel_b.update(attribs)
    morsel_b.set(*base_case)
    morsel_b['comment'] = 'bar'
    self.assertFalse(morsel_a == morsel_b)
    self.assertTrue(morsel_a != morsel_b)
    self.assertFalse(cookies.Morsel() == 1)
    self.assertTrue(cookies.Morsel() != 1)
    self.assertFalse(cookies.Morsel() == '')
    self.assertTrue(cookies.Morsel() != '')
    items = list(cookies.Morsel().items())
    self.assertFalse(cookies.Morsel() == items)
    self.assertTrue(cookies.Morsel() != items)
    morsel = cookies.Morsel()
    morsel.set(*base_case)
    morsel.update(attribs)
    self.assertTrue(morsel == dict(morsel))
    self.assertFalse(morsel != dict(morsel))
