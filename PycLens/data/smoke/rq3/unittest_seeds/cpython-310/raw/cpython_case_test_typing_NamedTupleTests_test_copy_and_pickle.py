# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_copy_and_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global Emp
    Emp = NamedTuple('Emp', [('name', str), ('cool', int)])
    for cls in (Emp, CoolEmployee, self.NestedEmployee):
        with self.subTest(cls=cls):
            jane = cls('jane', 37)
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                z = pickle.dumps(jane, proto)
                jane2 = pickle.loads(z)
                self.assertEqual(jane2, jane)
                self.assertIsInstance(jane2, cls)
            jane2 = copy(jane)
            self.assertEqual(jane2, jane)
            self.assertIsInstance(jane2, cls)
            jane2 = deepcopy(jane)
            self.assertEqual(jane2, jane)
            self.assertIsInstance(jane2, cls)
