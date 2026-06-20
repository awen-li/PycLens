# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ReloadTests_test_with_deleted_parent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from html import parser
    html = sys.modules.pop('html')

    def cleanup():
        sys.modules['html'] = html
    self.addCleanup(cleanup)
    with self.assertRaisesRegex(ImportError, 'html'):
        imp.reload(parser)
