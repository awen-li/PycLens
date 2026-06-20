# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_args_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (fd, fname) = tempfile.mkstemp()
    with open(fd, 'w', errors='surrogateescape') as fobj:
        fobj.write('#!%s\n' % support.unix_shell)
        fobj.write("exec '%s' -c 'import sys; sys.exit(47)'\n" % sys.executable)
    os.chmod(fname, 448)
    p = subprocess.Popen(fname)
    p.wait()
    os.remove(fname)
    self.assertEqual(p.returncode, 47)
