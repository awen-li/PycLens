# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Spam(types.SimpleNamespace):
        pass
    spam = Spam(ham=8, eggs=9)
    self.assertIs(type(spam), Spam)
    self.assertEqual(vars(spam), {'ham': 8, 'eggs': 9})
