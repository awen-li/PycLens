# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_multiset_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter(a=10, b=-2, c=0) + Counter()
    self.assertEqual(dict(c), dict(a=10))
    elements = 'abcd'
    for i in range(1000):
        p = Counter(dict(((elem, randrange(-2, 4)) for elem in elements)))
        p.update(e=1, f=-1, g=0)
        q = Counter(dict(((elem, randrange(-2, 4)) for elem in elements)))
        q.update(h=1, i=-1, j=0)
        for (counterop, numberop) in [(Counter.__add__, lambda x, y: max(0, x + y)), (Counter.__sub__, lambda x, y: max(0, x - y)), (Counter.__or__, lambda x, y: max(0, x, y)), (Counter.__and__, lambda x, y: max(0, min(x, y)))]:
            result = counterop(p, q)
            for x in elements:
                self.assertEqual(numberop(p[x], q[x]), result[x], (counterop, x, p, q))
            self.assertTrue((x > 0 for x in result.values()))
    elements = 'abcdef'
    for i in range(100):
        p = Counter(dict(((elem, randrange(0, 2)) for elem in elements)))
        q = Counter(dict(((elem, randrange(0, 2)) for elem in elements)))
        for (counterop, setop) in [(Counter.__sub__, set.__sub__), (Counter.__or__, set.__or__), (Counter.__and__, set.__and__)]:
            counter_result = counterop(p, q)
            set_result = setop(set(p.elements()), set(q.elements()))
            self.assertEqual(counter_result, dict.fromkeys(set_result, 1))
