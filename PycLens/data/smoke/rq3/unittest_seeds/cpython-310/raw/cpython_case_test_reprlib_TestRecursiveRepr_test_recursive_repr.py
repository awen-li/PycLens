# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: TestRecursiveRepr_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = MyContainer(list('abcde'))
    m.append(m)
    m.append('x')
    m.append(m)
    self.assertEqual(repr(m), '<a, b, c, d, e, ..., x, ...>')
    m = MyContainer2(list('abcde'))
    m.append(m)
    m.append('x')
    m.append(m)
    self.assertEqual(repr(m), '<a, b, c, d, e, +++, x, +++>')
