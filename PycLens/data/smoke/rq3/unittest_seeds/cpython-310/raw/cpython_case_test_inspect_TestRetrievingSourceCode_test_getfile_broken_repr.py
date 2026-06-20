# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getfile_broken_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ErrorRepr:

        def __repr__(self):
            raise Exception('xyz')
    er = ErrorRepr()
    with self.assertRaises(TypeError):
        inspect.getfile(er)
