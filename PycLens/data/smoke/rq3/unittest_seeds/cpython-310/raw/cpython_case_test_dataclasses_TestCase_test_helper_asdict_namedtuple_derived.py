# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_namedtuple_derived

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T(namedtuple('Tbase', 'a')):

        def my_a(self):
            return self.a

    @dataclass
    class C:
        f: T
    t = T(6)
    c = C(t)
    d = asdict(c)
    self.assertEqual(d, {'f': T(a=6)})
    self.assertIsNot(d['f'], t)
    self.assertEqual(d['f'].my_a(), 6)
