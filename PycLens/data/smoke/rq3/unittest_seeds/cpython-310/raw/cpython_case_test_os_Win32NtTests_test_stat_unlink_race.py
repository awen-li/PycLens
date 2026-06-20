# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32NtTests_test_stat_unlink_race

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    deadline = time.time() + 5
    command = textwrap.dedent('            import os\n            import sys\n            import time\n\n            filename = sys.argv[1]\n            deadline = float(sys.argv[2])\n\n            while time.time() < deadline:\n                try:\n                    with open(filename, "w") as f:\n                        pass\n                except OSError:\n                    pass\n                try:\n                    os.remove(filename)\n                except OSError:\n                    pass\n            ')
    with subprocess.Popen([sys.executable, '-c', command, filename, str(deadline)]) as proc:
        while time.time() < deadline:
            try:
                os.stat(filename)
            except FileNotFoundError as e:
                assert e.winerror == 2
        try:
            proc.wait(1)
        except subprocess.TimeoutExpired:
            proc.terminate()
