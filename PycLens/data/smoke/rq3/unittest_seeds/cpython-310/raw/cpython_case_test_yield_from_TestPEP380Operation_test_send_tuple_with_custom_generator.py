# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_send_tuple_with_custom_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyGen:

        def __iter__(self):
            return self

        def __next__(self):
            return 42

        def send(self, what):
            nonlocal v
            v = what
            return None

    def outer():
        v = (yield from MyGen())
    g = outer()
    next(g)
    v = None
    g.send((1, 2, 3, 4))
    self.assertEqual(v, (1, 2, 3, 4))
