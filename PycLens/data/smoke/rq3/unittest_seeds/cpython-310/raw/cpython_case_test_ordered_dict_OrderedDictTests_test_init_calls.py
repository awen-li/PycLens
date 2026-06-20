# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_init_calls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = []

    class Spam:

        def keys(self):
            calls.append('keys')
            return ()

        def items(self):
            calls.append('items')
            return ()
    self.OrderedDict(Spam())
    self.assertEqual(calls, ['keys'])
