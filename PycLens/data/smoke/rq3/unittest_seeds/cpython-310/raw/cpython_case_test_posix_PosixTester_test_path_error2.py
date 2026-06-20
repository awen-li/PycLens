# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_path_error2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in ('rename', 'replace', 'link'):
        function = getattr(os, name, None)
        if function is None:
            continue
        for dst in ('noodly2', os_helper.TESTFN):
            try:
                function('doesnotexistfilename', dst)
            except OSError as e:
                self.assertIn("'doesnotexistfilename' -> '{}'".format(dst), str(e))
                break
        else:
            self.fail('No valid path_error2() test for os.' + name)
