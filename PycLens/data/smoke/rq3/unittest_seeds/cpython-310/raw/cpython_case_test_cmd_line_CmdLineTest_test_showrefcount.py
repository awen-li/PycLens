# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_showrefcount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def run_python(*args):
        cmd = [sys.executable]
        cmd.extend(args)
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        (out, err) = p.communicate()
        p.stdout.close()
        p.stderr.close()
        rc = p.returncode
        self.assertEqual(rc, 0)
        return (rc, out, err)
    code = 'import sys; print(sys._xoptions)'
    (rc, out, err) = run_python('-c', code)
    self.assertEqual(out.rstrip(), b'{}')
    self.assertEqual(err, b'')
    (rc, out, err) = run_python('-X', 'showrefcount', '-c', code)
    self.assertEqual(out.rstrip(), b"{'showrefcount': True}")
    if Py_DEBUG:
        self.assertRegex(err, b'^\\[\\d+ refs, \\d+ blocks\\]')
    else:
        self.assertEqual(err, b'')
