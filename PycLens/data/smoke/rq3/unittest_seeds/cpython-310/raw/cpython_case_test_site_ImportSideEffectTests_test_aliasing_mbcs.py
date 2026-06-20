# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: ImportSideEffectTests_test_aliasing_mbcs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform == 'win32':
        import locale
        if locale.getdefaultlocale()[1].startswith('cp'):
            for value in encodings.aliases.aliases.values():
                if value == 'mbcs':
                    break
            else:
                self.fail('did not alias mbcs')
