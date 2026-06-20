# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppCmdlineTest_test_info_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    target = self.make_archive()
    args = [str(target), '--info']
    with self.assertRaises(SystemExit) as cm:
        zipapp.main(args)
    self.assertEqual(cm.exception.code, 0)
    self.assertEqual(mock_stdout.getvalue(), 'Interpreter: <none>\n')
