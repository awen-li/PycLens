# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: FunctionCalls_test_kwargs_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    od = collections.OrderedDict([('a', 1), ('b', 2)])
    od.move_to_end('a')
    expected = list(od.items())

    def fn(**kw):
        return kw
    res = fn(**od)
    self.assertIsInstance(res, dict)
    self.assertEqual(list(res.items()), expected)
