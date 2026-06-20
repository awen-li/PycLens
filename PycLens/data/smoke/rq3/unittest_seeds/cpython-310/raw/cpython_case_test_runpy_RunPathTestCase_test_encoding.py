# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunPathTestCase_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as script_dir:
        filename = os.path.join(script_dir, 'script.py')
        with open(filename, 'w', encoding='latin1') as f:
            f.write('\n#coding:latin1\ns = "non-ASCII: hé"\n')
        result = run_path(filename)
        self.assertEqual(result['s'], 'non-ASCII: hé')
