# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_union_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pydoc.describe(typing.Union[int, str]), '_UnionGenericAlias')
    doc = pydoc.render_doc(typing.Union[int, str], renderer=pydoc.plaintext)
    self.assertIn('_UnionGenericAlias in module typing', doc)
    self.assertIn('Union = typing.Union', doc)
    if typing.Union.__doc__:
        self.assertIn(typing.Union.__doc__.strip().splitlines()[0], doc)
    self.assertEqual(pydoc.describe(int | str), 'UnionType')
    doc = pydoc.render_doc(int | str, renderer=pydoc.plaintext)
    self.assertIn('UnionType in module types object', doc)
    self.assertIn('\nclass UnionType(builtins.object)', doc)
    self.assertIn(types.UnionType.__doc__.strip().splitlines()[0], doc)
