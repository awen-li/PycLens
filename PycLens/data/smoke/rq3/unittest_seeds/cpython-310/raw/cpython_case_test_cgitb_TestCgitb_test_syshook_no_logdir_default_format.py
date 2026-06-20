# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgitb.py
# case: TestCgitb_test_syshook_no_logdir_default_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as tracedir:
        (rc, out, err) = assert_python_failure('-c', 'import cgitb; cgitb.enable(logdir=%s); raise ValueError("Hello World")' % repr(tracedir), PYTHONIOENCODING='utf-8')
    out = out.decode()
    self.assertIn('ValueError', out)
    self.assertIn('Hello World', out)
    self.assertIn('<strong>&lt;module&gt;</strong>', out)
    self.assertIn('<p>', out)
    self.assertIn('</p>', out)
