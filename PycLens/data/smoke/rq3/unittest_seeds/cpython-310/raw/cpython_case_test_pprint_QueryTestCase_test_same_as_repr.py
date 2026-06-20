# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_same_as_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for simple in (0, 0, 0 + 0j, 0.0, '', b'', bytearray(), (), tuple2(), tuple3(), [], list2(), list3(), set(), set2(), set3(), frozenset(), frozenset2(), frozenset3(), {}, dict2(), dict3(), self.assertTrue, pprint, -6, -6, -6 - 6j, -1.5, 'x', b'x', bytearray(b'x'), (3,), [3], {3: 6}, (1, 2), [3, 4], {5: 6}, tuple2((1, 2)), tuple3((1, 2)), tuple3(range(100)), [3, 4], list2([3, 4]), list3([3, 4]), list3(range(100)), set({7}), set2({7}), set3({7}), frozenset({8}), frozenset2({8}), frozenset3({8}), dict2({5: 6}), dict3({5: 6}), range(10, -11, -1), True, False, None, ...):
        native = repr(simple)
        self.assertEqual(pprint.pformat(simple), native)
        self.assertEqual(pprint.pformat(simple, width=1, indent=0).replace('\n', ' '), native)
        self.assertEqual(pprint.pformat(simple, underscore_numbers=True), native)
        self.assertEqual(pprint.saferepr(simple), native)
