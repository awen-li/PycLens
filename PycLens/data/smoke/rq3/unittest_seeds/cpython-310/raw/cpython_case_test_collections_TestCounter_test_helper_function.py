# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_helper_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elems = list('abracadabra')
    d = dict()
    _count_elements(d, elems)
    self.assertEqual(d, {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1})
    m = OrderedDict()
    _count_elements(m, elems)
    self.assertEqual(m, OrderedDict([('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]))
    c = CounterSubclassWithSetItem('abracadabra')
    self.assertTrue(c.called)
    self.assertEqual(dict(c), {'a': 5, 'b': 2, 'c': 1, 'd': 1, 'r': 2})
    c = CounterSubclassWithGet('abracadabra')
    self.assertTrue(c.called)
    self.assertEqual(dict(c), {'a': 5, 'b': 2, 'c': 1, 'd': 1, 'r': 2})
