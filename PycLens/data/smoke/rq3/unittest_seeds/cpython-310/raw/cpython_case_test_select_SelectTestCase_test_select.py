# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_select.py
# case: SelectTestCase_test_select

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import time\n            for i in range(10):\n                print("testing...", flush=True)\n                time.sleep(0.050)\n        ')
    cmd = [sys.executable, '-I', '-c', code]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
        pipe = proc.stdout
        for timeout in (0, 1, 2, 4, 8, 16) + (None,) * 10:
            if support.verbose:
                print(f'timeout = {timeout}')
            (rfd, wfd, xfd) = select.select([pipe], [], [], timeout)
            self.assertEqual(wfd, [])
            self.assertEqual(xfd, [])
            if not rfd:
                continue
            if rfd == [pipe]:
                line = pipe.readline()
                if support.verbose:
                    print(repr(line))
                if not line:
                    if support.verbose:
                        print('EOF')
                    break
                continue
            self.fail('Unexpected return values from select():', rfd, wfd, xfd)
