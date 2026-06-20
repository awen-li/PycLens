# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_register_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test_jumbo(h, file):
        if h.startswith(b'eggs'):
            return 'ham'
    imghdr.tests.append(test_jumbo)
    self.addCleanup(imghdr.tests.pop)
    self.assertEqual(imghdr.what(None, b'eggs'), 'ham')
