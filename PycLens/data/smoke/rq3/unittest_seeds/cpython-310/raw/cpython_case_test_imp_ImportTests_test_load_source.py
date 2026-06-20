# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_load_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    modname = f'tmp{__name__}'
    mod = type(sys.modules[__name__])(modname)
    with support.swap_item(sys.modules, modname, mod):
        with self.assertRaisesRegex(ValueError, 'embedded null'):
            imp.load_source(modname, __file__ + '\x00')
