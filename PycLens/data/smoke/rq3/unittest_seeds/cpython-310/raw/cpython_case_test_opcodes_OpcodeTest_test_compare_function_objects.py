# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcodes.py
# case: OpcodeTest_test_compare_function_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = eval('lambda: None')
    g = eval('lambda: None')
    self.assertNotEqual(f, g)
    f = eval('lambda a: a')
    g = eval('lambda a: a')
    self.assertNotEqual(f, g)
    f = eval('lambda a=1: a')
    g = eval('lambda a=1: a')
    self.assertNotEqual(f, g)
    f = eval('lambda: 0')
    g = eval('lambda: 1')
    self.assertNotEqual(f, g)
    f = eval('lambda: None')
    g = eval('lambda a: None')
    self.assertNotEqual(f, g)
    f = eval('lambda a: None')
    g = eval('lambda b: None')
    self.assertNotEqual(f, g)
    f = eval('lambda a: None')
    g = eval('lambda a=None: None')
    self.assertNotEqual(f, g)
    f = eval('lambda a=0: None')
    g = eval('lambda a=1: None')
    self.assertNotEqual(f, g)
