# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocWithMetaClasses_test_DynamicClassAttribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __getattr__(self, name):
            if name == 'ham':
                return 'spam'
            return super().__getattr__(name)

    class DA(metaclass=Meta):

        @types.DynamicClassAttribute
        def ham(self):
            return 'eggs'
    expected_text_data_docstrings = tuple(('\n |      ' + s if s else '' for s in expected_data_docstrings))
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper(DA)
    expected_text = expected_dynamicattribute_pattern % ((__name__,) + expected_text_data_docstrings[:2])
    result = output.getvalue().strip()
    self.assertEqual(expected_text, result)
