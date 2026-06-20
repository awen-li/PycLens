# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_other_newlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compile('\r\n', '<test>', 'exec')
    compile('\r', '<test>', 'exec')
    compile('hi\r\nstuff\r\ndef f():\n    pass\r', '<test>', 'exec')
    compile('this_is\rreally_old_mac\rdef f():\n    pass', '<test>', 'exec')
