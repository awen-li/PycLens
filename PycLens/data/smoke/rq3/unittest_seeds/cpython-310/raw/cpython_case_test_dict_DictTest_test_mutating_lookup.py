# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_mutating_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NastyKey:
        mutate_dict = None

        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1

        def __eq__(self, other):
            if NastyKey.mutate_dict:
                (mydict, key) = NastyKey.mutate_dict
                NastyKey.mutate_dict = None
                del mydict[key]
            return self.value == other.value
    key1 = NastyKey(1)
    key2 = NastyKey(2)
    d = {key1: 1}
    NastyKey.mutate_dict = (d, key1)
    d[key2] = 2
    self.assertEqual(d, {key2: 2})
