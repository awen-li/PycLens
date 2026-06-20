# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_sort_unorderable_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 20
    keys = [Unorderable() for i in range(n)]
    random.shuffle(keys)
    skeys = sorted(keys, key=id)
    clean = lambda s: s.replace(' ', '').replace('\n', '')
    self.assertEqual(clean(pprint.pformat(set(keys))), '{' + ','.join(map(repr, skeys)) + '}')
    self.assertEqual(clean(pprint.pformat(frozenset(keys))), 'frozenset({' + ','.join(map(repr, skeys)) + '})')
    self.assertEqual(clean(pprint.pformat(dict.fromkeys(keys))), '{' + ','.join(('%r:None' % k for k in skeys)) + '}')
    self.assertEqual(pprint.pformat({Unorderable: 0, 1: 0}), '{1: 0, ' + repr(Unorderable) + ': 0}')
    keys = [(1,), (None,)]
    self.assertEqual(pprint.pformat(dict.fromkeys(keys, 0)), '{%r: 0, %r: 0}' % tuple(sorted(keys, key=id)))
