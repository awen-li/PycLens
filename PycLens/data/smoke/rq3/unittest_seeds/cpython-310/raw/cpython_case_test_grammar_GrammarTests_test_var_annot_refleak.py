# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_refleak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cns = CNS()
    nonloc_ns = {'__annotations__': cns}

    class CNS2:

        def __init__(self):
            self._dct = {'__annotations__': cns}

        def __setitem__(self, item, value):
            nonlocal nonloc_ns
            self._dct[item] = value
            nonloc_ns[item] = value

        def __getitem__(self, item):
            return self._dct[item]
    exec('X: str', {}, CNS2())
    self.assertEqual(nonloc_ns['__annotations__']['x'], str)
