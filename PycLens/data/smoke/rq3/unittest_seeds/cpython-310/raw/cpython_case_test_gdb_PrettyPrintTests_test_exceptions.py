# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (gdb_repr, gdb_output) = self.get_gdb_repr('\ntry:\n    raise RuntimeError("I am an error")\nexcept RuntimeError as e:\n    id(e)\n')
    self.assertEqual(gdb_repr, "RuntimeError('I am an error',)")
    (gdb_repr, gdb_output) = self.get_gdb_repr('\ntry:\n    a = 1 / 0\nexcept ZeroDivisionError as e:\n    id(e)\n')
    self.assertEqual(gdb_repr, "ZeroDivisionError('division by zero',)")
