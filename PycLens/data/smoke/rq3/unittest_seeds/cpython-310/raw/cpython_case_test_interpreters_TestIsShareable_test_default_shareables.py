# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestIsShareable_test_default_shareables

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    shareables = [None, b'spam', 'spam', 10, -10]
    for obj in shareables:
        with self.subTest(obj):
            shareable = interpreters.is_shareable(obj)
            self.assertTrue(shareable)
