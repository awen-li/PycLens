# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_invalid_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        class B(object):
            method = functools.partialmethod(None, 1)
    with self.assertRaises(TypeError):

        class B:
            method = functools.partialmethod()
    with self.assertRaises(TypeError):

        class B:
            method = functools.partialmethod(func=capture, a=1)
