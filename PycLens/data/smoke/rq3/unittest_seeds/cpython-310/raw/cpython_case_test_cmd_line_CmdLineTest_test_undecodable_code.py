# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_undecodable_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    undecodable = b'\xff'
    env = os.environ.copy()
    env['LC_ALL'] = 'C'
    env['PYTHONCOERCECLOCALE'] = '0'
    code = b'import locale; print(ascii("' + undecodable + b'"), locale.getpreferredencoding())'
    p = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
    (stdout, stderr) = p.communicate()
    if p.returncode == 1:
        pattern = b'Unable to decode the command from the command line:'
    elif p.returncode == 0:
        pattern = b"'\\xff' "
    else:
        raise AssertionError('Unknown exit code: %s, output=%a' % (p.returncode, stdout))
    if not stdout.startswith(pattern):
        raise AssertionError("%a doesn't start with %a" % (stdout, pattern))
