# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, *args, b, z=100, **kwargs):
        pass
    sig = inspect.signature(test)
    ba = sig.bind(10, 20, b=30, c=40, args=50, kwargs=60)
    self.assertEqual(tuple(ba.arguments.items()), (('a', 10), ('args', (20,)), ('b', 30), ('kwargs', {'c': 40, 'args': 50, 'kwargs': 60})))
    self.assertEqual(ba.kwargs, {'b': 30, 'c': 40, 'args': 50, 'kwargs': 60})
    self.assertEqual(ba.args, (10, 20))
