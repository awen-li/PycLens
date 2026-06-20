# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_getallocatedblocks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        import _testcapi
    except ImportError:
        with_pymalloc = support.with_pymalloc()
    else:
        try:
            alloc_name = _testcapi.pymem_getallocatorsname()
        except RuntimeError as exc:
            with_pymalloc = True
        else:
            with_pymalloc = alloc_name in ('pymalloc', 'pymalloc_debug')
    a = sys.getallocatedblocks()
    self.assertIs(type(a), int)
    if with_pymalloc:
        self.assertGreater(a, 0)
    else:
        self.assertGreaterEqual(a, 0)
    try:
        self.assertLess(a, sys.gettotalrefcount())
    except AttributeError:
        pass
    gc.collect()
    b = sys.getallocatedblocks()
    self.assertLessEqual(b, a)
    gc.collect()
    c = sys.getallocatedblocks()
    self.assertIn(c, range(b - 50, b + 50))
