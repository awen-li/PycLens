# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyclbr.py
# case: ReadmoduleTests_test_dotted_name_not_a_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ImportError, pyclbr.readmodule_ex, 'asyncio.foo')
