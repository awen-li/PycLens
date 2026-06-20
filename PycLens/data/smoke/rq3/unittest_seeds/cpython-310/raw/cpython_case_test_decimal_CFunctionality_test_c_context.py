# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CFunctionality_test_c_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = C.Context
    c = Context(flags=C.DecClamped, traps=C.DecRounded)
    self.assertEqual(c._flags, C.DecClamped)
    self.assertEqual(c._traps, C.DecRounded)
