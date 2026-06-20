# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getfullargspec_signature_annos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a: 'spam') -> 'ham':
        pass
    spec = inspect.getfullargspec(test)
    self.assertEqual(test.__annotations__, spec.annotations)

    def test():
        pass
    spec = inspect.getfullargspec(test)
    self.assertEqual(test.__annotations__, spec.annotations)
