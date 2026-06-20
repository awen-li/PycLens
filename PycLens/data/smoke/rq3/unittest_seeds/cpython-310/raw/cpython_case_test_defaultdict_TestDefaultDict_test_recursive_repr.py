# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class sub(defaultdict):

        def __init__(self):
            self.default_factory = self._factory

        def _factory(self):
            return []
    d = sub()
    self.assertRegex(repr(d), 'sub\\(<bound method .*sub\\._factory of sub\\(\\.\\.\\., \\{\\}\\)>, \\{\\}\\)')
