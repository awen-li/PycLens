# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocWithMetaClasses_test_buggy_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(type):

        def __dir__(cls):
            return ['__class__', '__name__', 'missing', 'here']

    class C(metaclass=M):
        here = 'present!'
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper(C)
    expected_text = expected_missingattribute_pattern % __name__
    result = output.getvalue().strip()
    self.assertEqual(expected_text, result)
