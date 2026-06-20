# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_device_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not sys.stdout.isatty():
        self.skipTest('sys.stdout is not a TTY')
    filename = 'out.txt'
    self.addCleanup(os_helper.unlink, filename)
    code = f'import os, sys; fd = sys.stdout.fileno(); out = open({filename!r}, "w", encoding="utf-8"); print(os.isatty(fd), os.device_encoding(fd), file=out); out.close()'
    cmd = [sys.executable, '-X', 'utf8', '-c', code]
    proc = subprocess.run(cmd, text=True)
    self.assertEqual(proc.returncode, 0, proc)
    with open(filename, encoding='utf8') as fp:
        out = fp.read().rstrip()
    self.assertEqual(out, 'True UTF-8')
