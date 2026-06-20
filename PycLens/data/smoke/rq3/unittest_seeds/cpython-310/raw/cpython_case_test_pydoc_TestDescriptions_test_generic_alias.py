# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_generic_alias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pydoc.describe(typing.List[int]), '_GenericAlias')
    doc = pydoc.render_doc(typing.List[int], renderer=pydoc.plaintext)
    self.assertIn('_GenericAlias in module typing', doc)
    self.assertIn('List = class list(object)', doc)
    self.assertIn(list.__doc__.strip().splitlines()[0], doc)
    self.assertEqual(pydoc.describe(list[int]), 'GenericAlias')
    doc = pydoc.render_doc(list[int], renderer=pydoc.plaintext)
    self.assertIn('GenericAlias in module builtins', doc)
    self.assertIn('\nclass list(object)', doc)
    self.assertIn(list.__doc__.strip().splitlines()[0], doc)
