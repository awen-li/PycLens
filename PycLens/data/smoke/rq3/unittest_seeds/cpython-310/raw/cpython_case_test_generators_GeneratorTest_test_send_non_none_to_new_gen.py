# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorTest_test_send_non_none_to_new_gen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        yield 1
    g = f()
    with self.assertRaises(TypeError):
        g.send(0)
    self.assertEqual(next(g), 1)
