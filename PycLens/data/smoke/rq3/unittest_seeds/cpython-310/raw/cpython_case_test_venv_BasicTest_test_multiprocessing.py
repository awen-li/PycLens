# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_multiprocessing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    skip_if_broken_multiprocessing_synchronize()
    rmtree(self.env_dir)
    self.run_with_capture(venv.create, self.env_dir)
    envpy = os.path.join(os.path.realpath(self.env_dir), self.bindir, self.exe)
    (out, err) = check_output([envpy, '-c', 'from multiprocessing import Pool; pool = Pool(1); print(pool.apply_async("Python".lower).get(3)); pool.terminate()'])
    self.assertEqual(out.strip(), 'python'.encode())
