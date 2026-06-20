# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_ioencoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = dict(os.environ)
    env['PYTHONIOENCODING'] = 'cp424'
    p = subprocess.Popen([sys.executable, '-c', 'print(chr(0xa2))'], stdout=subprocess.PIPE, env=env)
    out = p.communicate()[0].strip()
    expected = ('¢' + os.linesep).encode('cp424')
    self.assertEqual(out, expected)
    env['PYTHONIOENCODING'] = 'ascii:replace'
    p = subprocess.Popen([sys.executable, '-c', 'print(chr(0xa2))'], stdout=subprocess.PIPE, env=env)
    out = p.communicate()[0].strip()
    self.assertEqual(out, b'?')
    env['PYTHONIOENCODING'] = 'ascii'
    p = subprocess.Popen([sys.executable, '-c', 'print(chr(0xa2))'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    (out, err) = p.communicate()
    self.assertEqual(out, b'')
    self.assertIn(b'UnicodeEncodeError:', err)
    self.assertIn(b"'\\xa2'", err)
    env['PYTHONIOENCODING'] = 'ascii:'
    p = subprocess.Popen([sys.executable, '-c', 'print(chr(0xa2))'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    (out, err) = p.communicate()
    self.assertEqual(out, b'')
    self.assertIn(b'UnicodeEncodeError:', err)
    self.assertIn(b"'\\xa2'", err)
    env['PYTHONIOENCODING'] = ':surrogateescape'
    p = subprocess.Popen([sys.executable, '-c', 'print(chr(0xdcbd))'], stdout=subprocess.PIPE, env=env)
    out = p.communicate()[0].strip()
    self.assertEqual(out, b'\xbd')
