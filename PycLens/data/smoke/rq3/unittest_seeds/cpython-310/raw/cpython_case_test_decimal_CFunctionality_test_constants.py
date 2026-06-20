# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CFunctionality_test_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cond = (C.DecClamped, C.DecConversionSyntax, C.DecDivisionByZero, C.DecDivisionImpossible, C.DecDivisionUndefined, C.DecFpuError, C.DecInexact, C.DecInvalidContext, C.DecInvalidOperation, C.DecMallocError, C.DecFloatOperation, C.DecOverflow, C.DecRounded, C.DecSubnormal, C.DecUnderflow)
    self.assertEqual(C.DECIMAL32, 32)
    self.assertEqual(C.DECIMAL64, 64)
    self.assertEqual(C.DECIMAL128, 128)
    self.assertEqual(C.IEEE_CONTEXT_MAX_BITS, 512)
    for (i, v) in enumerate(cond):
        self.assertEqual(v, 1 << i)
    self.assertEqual(C.DecIEEEInvalidOperation, C.DecConversionSyntax | C.DecDivisionImpossible | C.DecDivisionUndefined | C.DecFpuError | C.DecInvalidContext | C.DecInvalidOperation | C.DecMallocError)
    self.assertEqual(C.DecErrors, C.DecIEEEInvalidOperation | C.DecDivisionByZero)
    self.assertEqual(C.DecTraps, C.DecErrors | C.DecOverflow | C.DecUnderflow)
