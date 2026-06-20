# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_corrupt_tp_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertSane('id(42)', 'set v->ob_type->tp_name=0xDEADBEEF', exprepr='42')
