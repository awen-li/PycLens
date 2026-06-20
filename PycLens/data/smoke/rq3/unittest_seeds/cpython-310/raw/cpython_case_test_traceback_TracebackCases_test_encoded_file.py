# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_encoded_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import sys, subprocess
    process = subprocess.Popen([sys.executable, '-c', 'import sys; print(sys.stdout.encoding)'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdout, stderr) = process.communicate()
    output_encoding = str(stdout, 'ascii').splitlines()[0]

    def do_test(firstlines, message, charset, lineno):
        try:
            with open(TESTFN, 'w', encoding=charset) as output:
                output.write("{0}if 1:\n                        import traceback;\n                        raise RuntimeError('{1}')\n                        ".format(firstlines, message))
            process = subprocess.Popen([sys.executable, TESTFN], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (stdout, stderr) = process.communicate()
            stdout = stdout.decode(output_encoding).splitlines()
        finally:
            unlink(TESTFN)
        encoded_message = message.encode(output_encoding, 'backslashreplace')
        message_ascii = encoded_message.decode(output_encoding)
        err_line = "raise RuntimeError('{0}')".format(message_ascii)
        err_msg = 'RuntimeError: {0}'.format(message_ascii)
        self.assertIn('line %s' % lineno, stdout[1], 'Invalid line number: {0!r} instead of {1}'.format(stdout[1], lineno))
        self.assertTrue(stdout[2].endswith(err_line), 'Invalid traceback line: {0!r} instead of {1!r}'.format(stdout[2], err_line))
        self.assertTrue(stdout[3] == err_msg, 'Invalid error message: {0!r} instead of {1!r}'.format(stdout[3], err_msg))
    do_test('', 'foo', 'ascii', 3)
    for charset in ('ascii', 'iso-8859-1', 'utf-8', 'GBK'):
        if charset == 'ascii':
            text = 'foo'
        elif charset == 'GBK':
            text = '丂儀'
        else:
            text = 'hé ho'
        do_test('# coding: {0}\n'.format(charset), text, charset, 4)
        do_test('#!shebang\n# coding: {0}\n'.format(charset), text, charset, 5)
        do_test(' \t\x0c\n# coding: {0}\n'.format(charset), text, charset, 5)
    do_test('x=0\n# coding: GBK\n', 'hé ho', 'utf-8', 5)
