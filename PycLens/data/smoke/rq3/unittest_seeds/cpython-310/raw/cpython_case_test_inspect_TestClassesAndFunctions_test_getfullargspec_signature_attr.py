# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getfullargspec_signature_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test():
        pass
    spam_param = inspect.Parameter('spam', inspect.Parameter.POSITIONAL_ONLY)
    test.__signature__ = inspect.Signature(parameters=(spam_param,))
    self.assertFullArgSpecEquals(test, ['spam'], formatted='(spam)')
