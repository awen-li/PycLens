# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: YieldFromTests_test_generator_gi_yieldfrom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def a():
        self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_RUNNING)
        self.assertIsNone(gen_b.gi_yieldfrom)
        yield
        self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_RUNNING)
        self.assertIsNone(gen_b.gi_yieldfrom)

    def b():
        self.assertIsNone(gen_b.gi_yieldfrom)
        yield from a()
        self.assertIsNone(gen_b.gi_yieldfrom)
        yield
        self.assertIsNone(gen_b.gi_yieldfrom)
    gen_b = b()
    self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_CREATED)
    self.assertIsNone(gen_b.gi_yieldfrom)
    gen_b.send(None)
    self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_SUSPENDED)
    self.assertEqual(gen_b.gi_yieldfrom.gi_code.co_name, 'a')
    gen_b.send(None)
    self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_SUSPENDED)
    self.assertIsNone(gen_b.gi_yieldfrom)
    [] = gen_b
    self.assertEqual(inspect.getgeneratorstate(gen_b), inspect.GEN_CLOSED)
    self.assertIsNone(gen_b.gi_yieldfrom)
