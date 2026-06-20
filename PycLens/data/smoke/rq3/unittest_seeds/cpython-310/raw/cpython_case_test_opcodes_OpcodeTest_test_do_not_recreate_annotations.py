# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcodes.py
# case: OpcodeTest_test_do_not_recreate_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.swap_item(globals(), '__annotations__', {}):
        del globals()['__annotations__']

        class C:
            del __annotations__
            with self.assertRaises(NameError):
                x: int
