# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_readrc_homedir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    save_home = os.environ.pop('HOME', None)
    with os_helper.temp_dir() as temp_dir, patch('os.path.expanduser'):
        rc_path = os.path.join(temp_dir, '.pdbrc')
        os.path.expanduser.return_value = rc_path
        try:
            with open(rc_path, 'w') as f:
                f.write('invalid')
            self.assertEqual(pdb.Pdb().rcLines[0], 'invalid')
        finally:
            if save_home is not None:
                os.environ['HOME'] = save_home
