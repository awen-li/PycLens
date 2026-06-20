# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestValueErrors_test_mapping_pattern_checks_duplicate_key_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Keys:
        KEY = 'a'
    x = {'a': 0, 'b': 1}
    w = y = z = None
    with self.assertRaises(ValueError):
        match x:
            case {Keys.KEY: y, 'a': z}:
                w = 0
    self.assertIs(w, None)
    self.assertIs(y, None)
    self.assertIs(z, None)
