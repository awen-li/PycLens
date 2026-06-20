# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_readrc_kwarg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent("\n            import pdb; pdb.Pdb(readrc=False).set_trace()\n\n            print('hello')\n        ")
    save_home = os.environ.pop('HOME', None)
    try:
        with os_helper.temp_cwd():
            with open('.pdbrc', 'w') as f:
                f.write('invalid\n')
            with open('main.py', 'w') as f:
                f.write(script)
            cmd = [sys.executable, 'main.py']
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            with proc:
                (stdout, stderr) = proc.communicate(b'q\n')
                self.assertNotIn(b"NameError: name 'invalid' is not defined", stdout)
    finally:
        if save_home is not None:
            os.environ['HOME'] = save_home
