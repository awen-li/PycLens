# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyclbr.py
# case: ReadmoduleTests_test_module_has_no_spec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module_name = 'doesnotexist'
    assert module_name not in pyclbr._modules
    with test_importlib_util.uncache(module_name):
        with self.assertRaises(ModuleNotFoundError):
            pyclbr.readmodule_ex(module_name)
