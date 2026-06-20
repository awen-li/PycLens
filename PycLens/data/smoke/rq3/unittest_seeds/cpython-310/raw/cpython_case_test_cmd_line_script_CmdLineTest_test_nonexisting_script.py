# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_nonexisting_script

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = 'nonexistingscript.py'
    self.assertFalse(os.path.exists(script))
    proc = spawn_python(script, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()
    self.assertIn(": can't open file ", err)
    self.assertNotEqual(proc.returncode, 0)
