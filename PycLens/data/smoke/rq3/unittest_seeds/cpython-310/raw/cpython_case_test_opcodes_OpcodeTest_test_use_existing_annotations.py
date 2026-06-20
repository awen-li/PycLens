# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcodes.py
# case: OpcodeTest_test_use_existing_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {'__annotations__': {1: 2}}
    exec('x: int', ns)
    self.assertEqual(ns['__annotations__'], {'x': int, 1: 2})
