# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_listcomps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nums = [1, 2, 3, 4, 5]
    strs = ['Apple', 'Banana', 'Coconut']
    spcs = ['  Apple', ' Banana ', 'Coco  nut  ']
    self.assertEqual([s.strip() for s in spcs], ['Apple', 'Banana', 'Coco  nut'])
    self.assertEqual([3 * x for x in nums], [3, 6, 9, 12, 15])
    self.assertEqual([x for x in nums if x > 2], [3, 4, 5])
    self.assertEqual([(i, s) for i in nums for s in strs], [(1, 'Apple'), (1, 'Banana'), (1, 'Coconut'), (2, 'Apple'), (2, 'Banana'), (2, 'Coconut'), (3, 'Apple'), (3, 'Banana'), (3, 'Coconut'), (4, 'Apple'), (4, 'Banana'), (4, 'Coconut'), (5, 'Apple'), (5, 'Banana'), (5, 'Coconut')])
    self.assertEqual([(i, s) for i in nums for s in [f for f in strs if 'n' in f]], [(1, 'Banana'), (1, 'Coconut'), (2, 'Banana'), (2, 'Coconut'), (3, 'Banana'), (3, 'Coconut'), (4, 'Banana'), (4, 'Coconut'), (5, 'Banana'), (5, 'Coconut')])
    self.assertEqual([(lambda a: [a ** i for i in range(a + 1)])(j) for j in range(5)], [[1], [1, 1], [1, 2, 4], [1, 3, 9, 27], [1, 4, 16, 64, 256]])

    def test_in_func(l):
        return [0 < x < 3 for x in l if x > 2]
    self.assertEqual(test_in_func(nums), [False, False, False])

    def test_nested_front():
        self.assertEqual([[y for y in [x, x + 1]] for x in [1, 3, 5]], [[1, 2], [3, 4], [5, 6]])
    test_nested_front()
    check_syntax_error(self, '[i, s for i in nums for s in strs]')
    check_syntax_error(self, '[x if y]')
    suppliers = [(1, 'Boeing'), (2, 'Ford'), (3, 'Macdonalds')]
    parts = [(10, 'Airliner'), (20, 'Engine'), (30, 'Cheeseburger')]
    suppart = [(1, 10), (1, 20), (2, 20), (3, 30)]
    x = [(sname, pname) for (sno, sname) in suppliers for (pno, pname) in parts for (sp_sno, sp_pno) in suppart if sno == sp_sno and pno == sp_pno]
    self.assertEqual(x, [('Boeing', 'Airliner'), ('Boeing', 'Engine'), ('Ford', 'Engine'), ('Macdonalds', 'Cheeseburger')])
