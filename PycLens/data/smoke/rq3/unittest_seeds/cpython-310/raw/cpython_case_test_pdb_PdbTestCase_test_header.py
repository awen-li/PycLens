# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = StringIO()
    header = 'Nobody expects... blah, blah, blah'
    with ExitStack() as resources:
        resources.enter_context(patch('sys.stdout', stdout))
        resources.enter_context(patch.object(pdb.Pdb, 'set_trace'))
        pdb.set_trace(header=header)
    self.assertEqual(stdout.getvalue(), header + '\n')
