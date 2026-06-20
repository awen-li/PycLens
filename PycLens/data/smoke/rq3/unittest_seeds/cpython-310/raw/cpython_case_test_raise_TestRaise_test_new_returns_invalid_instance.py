# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_new_returns_invalid_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyException(Exception):

        def __new__(cls, *args):
            return object()
    with self.assertRaises(TypeError):
        raise MyException
