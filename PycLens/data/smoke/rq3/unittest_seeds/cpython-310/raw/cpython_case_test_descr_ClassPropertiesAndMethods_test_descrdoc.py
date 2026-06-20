# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_descrdoc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _io import FileIO

    def check(descr, what):
        self.assertEqual(descr.__doc__, what)
    check(FileIO.closed, 'True if the file is closed')
    check(complex.real, 'the real part of a complex number')
