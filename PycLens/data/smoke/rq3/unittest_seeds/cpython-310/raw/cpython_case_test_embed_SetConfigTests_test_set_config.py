# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: SetConfigTests_test_set_config

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmd = [sys.executable, '-I', '-m', 'test._test_embed_set_config']
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.assertEqual(proc.returncode, 0, (proc.returncode, proc.stdout, proc.stderr))
