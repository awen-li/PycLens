# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_builtin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in ('str', 'str.translate', 'builtins.str', 'builtins.str.translate'):
        self.assertIsNotNone(pydoc.locate(name))
        try:
            pydoc.render_doc(name)
        except ImportError:
            self.fail('finding the doc of {!r} failed'.format(name))
    for name in ('notbuiltins', 'strrr', 'strr.translate', 'str.trrrranslate', 'builtins.strrr', 'builtins.str.trrranslate'):
        self.assertIsNone(pydoc.locate(name))
        self.assertRaises(ImportError, pydoc.render_doc, name)
