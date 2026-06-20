# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_hash_randomization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.verify_valid_flag('-R')
    hashes = []
    if os.environ.get('PYTHONHASHSEED', 'random') != 'random':
        env = dict(os.environ)
        del env['PYTHONHASHSEED']
        env['__cleanenv'] = '1'
    else:
        env = {}
    for i in range(3):
        code = 'print(hash("spam"))'
        (rc, out, err) = assert_python_ok('-c', code, **env)
        self.assertEqual(rc, 0)
        hashes.append(out)
    hashes = sorted(set(hashes))
    self.assertGreater(len(hashes), 1, msg='3 runs produced an identical random hash  for "spam": {}'.format(hashes))
    code = 'import sys; print("random is", sys.flags.hash_randomization)'
    (rc, out, err) = assert_python_ok('-c', code, PYTHONHASHSEED='')
    self.assertIn(b'random is 1', out)
    (rc, out, err) = assert_python_ok('-c', code, PYTHONHASHSEED='random')
    self.assertIn(b'random is 1', out)
    (rc, out, err) = assert_python_ok('-c', code, PYTHONHASHSEED='0')
    self.assertIn(b'random is 0', out)
    (rc, out, err) = assert_python_ok('-R', '-c', code, PYTHONHASHSEED='0')
    self.assertIn(b'random is 1', out)
