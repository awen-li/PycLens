# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_open_non_inheritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fileobj = open(__file__, encoding='utf-8')
    with fileobj:
        self.assertFalse(os.get_inheritable(fileobj.fileno()))
