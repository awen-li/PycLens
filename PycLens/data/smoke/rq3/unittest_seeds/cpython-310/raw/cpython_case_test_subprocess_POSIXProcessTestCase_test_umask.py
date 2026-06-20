# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_umask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmpdir = None
    try:
        tmpdir = tempfile.mkdtemp()
        name = os.path.join(tmpdir, 'beans')
        subprocess.check_call([sys.executable, '-c', f"open({name!r}, 'w').close()"], umask=43)
        st_mode = os.stat(name).st_mode & 438
        expected_mode = 404
        self.assertEqual(expected_mode, st_mode, msg=f'{oct(expected_mode)} != {oct(st_mode)}')
    finally:
        if tmpdir is not None:
            shutil.rmtree(tmpdir)
