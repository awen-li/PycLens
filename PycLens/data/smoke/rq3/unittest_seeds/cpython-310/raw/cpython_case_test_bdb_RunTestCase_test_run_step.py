# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: RunTestCase_test_run_step

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\n            lno = 2\n        '
    self.expect_set = [('line', 2, '<module>'), ('step',), ('return', 2, '<module>'), ('quit',)]
    with TracerRun(self) as tracer:
        tracer.run(compile(textwrap.dedent(code), '<string>', 'exec'))
