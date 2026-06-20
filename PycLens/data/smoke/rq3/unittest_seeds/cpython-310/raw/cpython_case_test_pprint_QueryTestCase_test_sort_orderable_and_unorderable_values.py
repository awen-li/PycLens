# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_sort_orderable_and_unorderable_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = Unorderable()
    b = Orderable(hash(a))
    self.assertLess(a, b)
    self.assertLess(str(type(b)), str(type(a)))
    self.assertEqual(sorted([b, a]), [a, b])
    self.assertEqual(sorted([a, b]), [a, b])
    self.assertEqual(pprint.pformat(set([b, a]), width=1), '{%r,\n %r}' % (a, b))
    self.assertEqual(pprint.pformat(set([a, b]), width=1), '{%r,\n %r}' % (a, b))
    self.assertEqual(pprint.pformat(dict.fromkeys([b, a]), width=1), '{%r: None,\n %r: None}' % (a, b))
    self.assertEqual(pprint.pformat(dict.fromkeys([a, b]), width=1), '{%r: None,\n %r: None}' % (a, b))
