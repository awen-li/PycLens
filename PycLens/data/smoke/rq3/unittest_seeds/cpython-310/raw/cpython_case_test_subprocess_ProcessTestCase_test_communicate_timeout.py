# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os,time;sys.stderr.write("pineapple\\n");time.sleep(1);sys.stderr.write("pear\\n");sys.stdout.write(sys.stdin.read())'], universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.assertRaises(subprocess.TimeoutExpired, p.communicate, 'banana', timeout=0.3)
    (stdout, stderr) = p.communicate()
    self.assertEqual(stdout, 'banana')
    self.assertEqual(stderr.encode(), b'pineapple\npear\n')
