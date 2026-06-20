# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: ImportSideEffectTests_test_sitecustomize_executed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if 'sitecustomize' not in sys.modules:
        try:
            import sitecustomize
        except ImportError:
            pass
        else:
            self.fail('sitecustomize not imported automatically')
