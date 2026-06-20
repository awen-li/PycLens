# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_bytes_program

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    abs_program = os.fsencode(ZERO_RETURN_CMD[0])
    args = list(ZERO_RETURN_CMD[1:])
    (path, program) = os.path.split(ZERO_RETURN_CMD[0])
    program = os.fsencode(program)
    exitcode = subprocess.call([abs_program] + args)
    self.assertEqual(exitcode, 0)
    cmd = b"'%s' %s" % (abs_program, ' '.join(args).encode('utf-8'))
    exitcode = subprocess.call(cmd, shell=True)
    self.assertEqual(exitcode, 0)
    env = os.environ.copy()
    env['PATH'] = path
    exitcode = subprocess.call([program] + args, env=env)
    self.assertEqual(exitcode, 0)
    envb = os.environb.copy()
    envb[b'PATH'] = os.fsencode(path)
    exitcode = subprocess.call([program] + args, env=envb)
    self.assertEqual(exitcode, 0)
