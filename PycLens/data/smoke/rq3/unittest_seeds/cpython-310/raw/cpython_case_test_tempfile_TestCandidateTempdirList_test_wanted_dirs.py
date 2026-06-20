# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestCandidateTempdirList_test_wanted_dirs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        for envname in ('TMPDIR', 'TEMP', 'TMP'):
            dirname = os.getenv(envname)
            if not dirname:
                env[envname] = os.path.abspath(envname)
        cand = tempfile._candidate_tempdir_list()
        for envname in ('TMPDIR', 'TEMP', 'TMP'):
            dirname = os.getenv(envname)
            if not dirname:
                raise ValueError
            self.assertIn(dirname, cand)
        try:
            dirname = os.getcwd()
        except (AttributeError, OSError):
            dirname = os.curdir
        self.assertIn(dirname, cand)
