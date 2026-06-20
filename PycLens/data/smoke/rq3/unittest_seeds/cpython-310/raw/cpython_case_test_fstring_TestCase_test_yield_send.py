# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_yield_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fn(x):
        yield f'x:{(yield (lambda i: x * i))}'
    g = fn(10)
    the_lambda = next(g)
    self.assertEqual(the_lambda(4), 40)
    self.assertEqual(g.send('string'), 'x:string')
