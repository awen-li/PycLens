# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_special_form

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pydoc.describe(typing.Any), '_SpecialForm')
    doc = pydoc.render_doc(typing.Any, renderer=pydoc.plaintext)
    self.assertIn('_SpecialForm in module typing', doc)
    if typing.Any.__doc__:
        self.assertIn('Any = typing.Any', doc)
        self.assertIn(typing.Any.__doc__.strip().splitlines()[0], doc)
    else:
        self.assertIn('Any = class _SpecialForm(_Final)', doc)
