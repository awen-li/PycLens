# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_container_repr_override_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 1000
    for cont in (list_custom_repr(), list_custom_repr([1, 2, 3]), list_custom_repr(range(N)), tuple_custom_repr(), tuple_custom_repr([1, 2, 3]), tuple_custom_repr(range(N)), set_custom_repr(), set_custom_repr([1, 2, 3]), set_custom_repr(range(N)), frozenset_custom_repr(), frozenset_custom_repr([1, 2, 3]), frozenset_custom_repr(range(N)), dict_custom_repr(), dict_custom_repr({5: 6}), dict_custom_repr(zip(range(N), range(N)))):
        native = repr(cont)
        expected = '*' * len(native)
        self.assertEqual(pprint.pformat(cont), expected)
        self.assertEqual(pprint.pformat(cont, width=1, indent=0), expected)
        self.assertEqual(pprint.saferepr(cont), expected)
