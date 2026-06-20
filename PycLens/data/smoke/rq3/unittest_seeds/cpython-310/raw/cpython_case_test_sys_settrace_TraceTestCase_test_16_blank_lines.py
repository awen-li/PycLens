# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_16_blank_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    namespace = {}
    exec('def f():\n' + '\n' * 256 + '    pass', namespace)
    self.run_and_compare(namespace['f'], [(0, 'call'), (257, 'line'), (257, 'return')])
