# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_isdisjoint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(s1, s2):
        """Pure python equivalent of isdisjoint()"""
        return not set(s1).intersection(s2)
    for larg in ('', 'a', 'ab', 'abc', 'ababac', 'cdc', 'cc', 'efgfe', 'ccb', 'ef'):
        s1 = self.thetype(larg)
        for rarg in ('', 'a', 'ab', 'abc', 'ababac', 'cdc', 'cc', 'efgfe', 'ccb', 'ef'):
            for C in (set, frozenset, dict.fromkeys, str, list, tuple):
                s2 = C(rarg)
                actual = s1.isdisjoint(s2)
                expected = f(s1, s2)
                self.assertEqual(actual, expected)
                self.assertTrue(actual is True or actual is False)
