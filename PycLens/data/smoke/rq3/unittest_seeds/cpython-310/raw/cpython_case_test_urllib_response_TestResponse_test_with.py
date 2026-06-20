# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib_response.py
# case: TestResponse_test_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    addbase = urllib.response.addbase(self.fp)
    self.assertIsInstance(addbase, tempfile._TemporaryFileWrapper)

    def f():
        with addbase as spam:
            pass
    self.assertFalse(self.fp.closed)
    f()
    self.assertTrue(self.fp.closed)
    self.assertRaises(ValueError, f)
