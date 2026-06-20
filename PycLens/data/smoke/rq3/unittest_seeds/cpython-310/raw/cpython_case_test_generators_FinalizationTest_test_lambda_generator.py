# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: FinalizationTest_test_lambda_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = lambda : (yield 1)

    def g():
        return (yield 1)
    f2 = lambda : (yield from g())

    def g2():
        return (yield from g())
    f3 = lambda : (yield from f())

    def g3():
        return (yield from f())
    for gen_fun in (f, g, f2, g2, f3, g3):
        gen = gen_fun()
        self.assertEqual(next(gen), 1)
        with self.assertRaises(StopIteration) as cm:
            gen.send(2)
        self.assertEqual(cm.exception.value, 2)
