# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_profile.py
# case: ProfileTest_test_output_file_when_changing_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as tmpdir, change_cwd(tmpdir):
        os.mkdir('dest')
        with open('demo.py', 'w', encoding='utf-8') as f:
            f.write('import os; os.chdir("dest")')
        assert_python_ok('-m', self.profilermodule.__name__, '-o', 'out.pstats', 'demo.py')
        self.assertTrue(os.path.exists('out.pstats'))
