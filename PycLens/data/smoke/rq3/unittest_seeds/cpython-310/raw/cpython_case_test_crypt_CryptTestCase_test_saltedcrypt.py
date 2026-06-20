# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_saltedcrypt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for method in crypt.methods:
        cr = crypt.crypt('assword', method)
        self.assertEqual(len(cr), method.total_size)
        cr2 = crypt.crypt('assword', cr)
        self.assertEqual(cr2, cr)
        cr = crypt.crypt('assword', crypt.mksalt(method))
        self.assertEqual(len(cr), method.total_size)
