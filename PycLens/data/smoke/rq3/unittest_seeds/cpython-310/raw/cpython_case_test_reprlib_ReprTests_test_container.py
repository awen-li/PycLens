# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_container

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from array import array
    from collections import deque
    eq = self.assertEqual
    eq(r(()), '()')
    eq(r((1,)), '(1,)')
    eq(r((1, 2, 3)), '(1, 2, 3)')
    eq(r((1, 2, 3, 4, 5, 6)), '(1, 2, 3, 4, 5, 6)')
    eq(r((1, 2, 3, 4, 5, 6, 7)), '(1, 2, 3, 4, 5, 6, ...)')
    eq(r([]), '[]')
    eq(r([1]), '[1]')
    eq(r([1, 2, 3]), '[1, 2, 3]')
    eq(r([1, 2, 3, 4, 5, 6]), '[1, 2, 3, 4, 5, 6]')
    eq(r([1, 2, 3, 4, 5, 6, 7]), '[1, 2, 3, 4, 5, 6, ...]')
    eq(r(set([])), 'set()')
    eq(r(set([1])), '{1}')
    eq(r(set([1, 2, 3])), '{1, 2, 3}')
    eq(r(set([1, 2, 3, 4, 5, 6])), '{1, 2, 3, 4, 5, 6}')
    eq(r(set([1, 2, 3, 4, 5, 6, 7])), '{1, 2, 3, 4, 5, 6, ...}')
    eq(r(frozenset([])), 'frozenset()')
    eq(r(frozenset([1])), 'frozenset({1})')
    eq(r(frozenset([1, 2, 3])), 'frozenset({1, 2, 3})')
    eq(r(frozenset([1, 2, 3, 4, 5, 6])), 'frozenset({1, 2, 3, 4, 5, 6})')
    eq(r(frozenset([1, 2, 3, 4, 5, 6, 7])), 'frozenset({1, 2, 3, 4, 5, 6, ...})')
    eq(r(deque([1, 2, 3, 4, 5, 6, 7])), 'deque([1, 2, 3, 4, 5, 6, ...])')
    eq(r({}), '{}')
    d = {'alice': 1, 'bob': 2, 'charles': 3, 'dave': 4}
    eq(r(d), "{'alice': 1, 'bob': 2, 'charles': 3, 'dave': 4}")
    d['arthur'] = 1
    eq(r(d), "{'alice': 1, 'arthur': 1, 'bob': 2, 'charles': 3, ...}")
    eq(r(array('i')), "array('i')")
    eq(r(array('i', [1])), "array('i', [1])")
    eq(r(array('i', [1, 2])), "array('i', [1, 2])")
    eq(r(array('i', [1, 2, 3])), "array('i', [1, 2, 3])")
    eq(r(array('i', [1, 2, 3, 4])), "array('i', [1, 2, 3, 4])")
    eq(r(array('i', [1, 2, 3, 4, 5])), "array('i', [1, 2, 3, 4, 5])")
    eq(r(array('i', [1, 2, 3, 4, 5, 6])), "array('i', [1, 2, 3, 4, 5, ...])")
