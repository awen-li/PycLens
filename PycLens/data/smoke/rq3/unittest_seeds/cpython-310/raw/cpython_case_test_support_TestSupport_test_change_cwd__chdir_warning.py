# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_change_cwd__chdir_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = TESTFN + '_does_not_exist'
    with warnings_helper.check_warnings() as recorder:
        with os_helper.change_cwd(path=path, quiet=True):
            pass
        messages = [str(w.message) for w in recorder.warnings]
    self.assertEqual(len(messages), 1, messages)
    msg = messages[0]
    self.assertTrue(msg.startswith(f'tests may fail, unable to change the current working directory to {path!r}: '), msg)
