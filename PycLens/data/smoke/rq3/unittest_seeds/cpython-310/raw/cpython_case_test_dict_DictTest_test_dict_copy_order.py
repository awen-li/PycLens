# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_dict_copy_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    od = collections.OrderedDict([('a', 1), ('b', 2)])
    od.move_to_end('a')
    expected = list(od.items())
    copy = dict(od)
    self.assertEqual(list(copy.items()), expected)

    class CustomDict(dict):
        pass
    pairs = [('a', 1), ('b', 2), ('c', 3)]
    d = CustomDict(pairs)
    self.assertEqual(pairs, list(dict(d).items()))

    class CustomReversedDict(dict):

        def keys(self):
            return reversed(list(dict.keys(self)))
        __iter__ = keys

        def items(self):
            return reversed(dict.items(self))
    d = CustomReversedDict(pairs)
    self.assertEqual(pairs[::-1], list(dict(d).items()))
