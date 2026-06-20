# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_inplace_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elements = 'abcd'
    for i in range(1000):
        p = Counter(dict(((elem, randrange(-2, 4)) for elem in elements)))
        p.update(e=1, f=-1, g=0)
        q = Counter(dict(((elem, randrange(-2, 4)) for elem in elements)))
        q.update(h=1, i=-1, j=0)
        for (inplace_op, regular_op) in [(Counter.__iadd__, Counter.__add__), (Counter.__isub__, Counter.__sub__), (Counter.__ior__, Counter.__or__), (Counter.__iand__, Counter.__and__)]:
            c = p.copy()
            c_id = id(c)
            regular_result = regular_op(c, q)
            inplace_result = inplace_op(c, q)
            self.assertEqual(inplace_result, regular_result)
            self.assertEqual(id(inplace_result), c_id)
