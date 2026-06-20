# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_no_leaking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not mswindows:
        max_handles = 1026
    else:
        max_handles = 2050
    handles = []
    tmpdir = tempfile.mkdtemp()
    try:
        for i in range(max_handles):
            try:
                tmpfile = os.path.join(tmpdir, os_helper.TESTFN)
                handles.append(os.open(tmpfile, os.O_WRONLY | os.O_CREAT))
            except OSError as e:
                if e.errno != errno.EMFILE:
                    raise
                break
        else:
            self.skipTest('failed to reach the file descriptor limit (tried %d)' % max_handles)
        for i in range(10):
            os.close(handles.pop())
        for i in range(15):
            p = subprocess.Popen([sys.executable, '-c', 'import sys;sys.stdout.write(sys.stdin.read())'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            data = p.communicate(b'lime')[0]
            self.assertEqual(data, b'lime')
    finally:
        for h in handles:
            os.close(h)
        shutil.rmtree(tmpdir)
