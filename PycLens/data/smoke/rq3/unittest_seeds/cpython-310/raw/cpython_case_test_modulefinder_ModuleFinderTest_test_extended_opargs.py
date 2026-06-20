# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_modulefinder.py
# case: ModuleFinderTest_test_extended_opargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    extended_opargs_test = ['a', ['a', 'b'], [], [], 'a.py\n                                %r\n                                import b\nb.py\n' % list(range(2 ** 16))]
    self._do_test(extended_opargs_test)
