# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_annotation_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'def f(%s): pass'
    s %= ', '.join(('a%d:%d' % (i, i) for i in range(300)))
    compile(s, '?', 'exec')
