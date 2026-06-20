# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_namedtuple_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        f: dict
    T = namedtuple('T', 'a')
    c = C({T('an a'): 0})
    self.assertEqual(asdict(c), {'f': {T(a='an a'): 0}})
