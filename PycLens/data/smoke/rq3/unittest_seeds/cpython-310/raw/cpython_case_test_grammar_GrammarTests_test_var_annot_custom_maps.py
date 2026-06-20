# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_custom_maps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {'__annotations__': CNS()}
    exec('X: int; Z: str = "Z"; (w): complex = 1j', ns)
    self.assertEqual(ns['__annotations__']['x'], int)
    self.assertEqual(ns['__annotations__']['z'], str)
    with self.assertRaises(KeyError):
        ns['__annotations__']['w']
    nonloc_ns = {}

    class CNS2:

        def __init__(self):
            self._dct = {}

        def __setitem__(self, item, value):
            nonlocal nonloc_ns
            self._dct[item] = value
            nonloc_ns[item] = value

        def __getitem__(self, item):
            return self._dct[item]
    exec('x: int = 1', {}, CNS2())
    self.assertEqual(nonloc_ns['__annotations__']['x'], int)
