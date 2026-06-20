# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_crypt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cr = crypt.crypt('mypassword')
    cr2 = crypt.crypt('mypassword', cr)
    self.assertEqual(cr2, cr)
    cr = crypt.crypt('mypassword', 'ab')
    if cr is not None:
        cr2 = crypt.crypt('mypassword', cr)
        self.assertEqual(cr2, cr)
