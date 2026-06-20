# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocWithMetaClasses_test_virtualClassAttributeWithOneMeta

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __dir__(cls):
            return ['__class__', '__module__', '__name__', 'LIFE']

        def __getattr__(self, name):
            if name == 'LIFE':
                return 42
            return super().__getattr(name)

    class Class(metaclass=Meta):
        pass
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper(Class)
    expected_text = expected_virtualattribute_pattern1 % __name__
    result = output.getvalue().strip()
    self.assertEqual(expected_text, result)
