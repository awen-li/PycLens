# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_dunder_is_original

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    names = [name for name in dir(operator) if not name.startswith('_')]
    for name in names:
        orig = getattr(operator, name)
        dunder = getattr(operator, '__' + name.strip('_') + '__', None)
        if dunder:
            self.assertIs(dunder, orig)
