# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_exception_value_crash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g1():
        yield from g2()

    def g2():
        yield 'g2'
        return [42]
    self.assertEqual(list(g1()), ['g2'])
