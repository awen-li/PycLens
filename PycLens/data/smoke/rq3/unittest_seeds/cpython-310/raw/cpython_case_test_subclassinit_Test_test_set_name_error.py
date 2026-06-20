# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_set_name_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descriptor:

        def __set_name__(self, owner, name):
            1 / 0
    with self.assertRaises(RuntimeError) as cm:

        class NotGoingToWork:
            attr = Descriptor()
    exc = cm.exception
    self.assertRegex(str(exc), '\\bNotGoingToWork\\b')
    self.assertRegex(str(exc), '\\battr\\b')
    self.assertRegex(str(exc), '\\bDescriptor\\b')
    self.assertIsInstance(exc.__cause__, ZeroDivisionError)
