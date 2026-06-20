# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_catching_exception_from_subgen_and_returning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def inner():
        try:
            yield 1
        except ValueError:
            trace.append('inner caught ValueError')
        return value

    def outer():
        v = (yield from inner())
        trace.append('inner returned %r to outer' % (v,))
        yield v
    for value in (2, (2,), StopIteration(2)):
        trace = []
        g = outer()
        trace.append(next(g))
        trace.append(repr(g.throw(ValueError)))
        self.assertEqual(trace, [1, 'inner caught ValueError', 'inner returned %r to outer' % (value,), repr(value)])
