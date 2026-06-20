# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_readline.py
# case: TestReadline_test_history_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    history_size = 10
    with temp_dir() as test_dir:
        inputrc = os.path.join(test_dir, 'inputrc')
        with open(inputrc, 'wb') as f:
            f.write(b'set history-size %d\n' % history_size)
        history_file = os.path.join(test_dir, 'history')
        with open(history_file, 'wb') as f:
            data = b''.join((b'item %d\n' % i for i in range(history_size * 2)))
            f.write(data)
        script = '\nimport os\nimport readline\n\nhistory_file = os.environ["HISTORY_FILE"]\nreadline.read_history_file(history_file)\ninput()\nreadline.write_history_file(history_file)\n'
        env = dict(os.environ)
        env['INPUTRC'] = inputrc
        env['HISTORY_FILE'] = history_file
        run_pty(script, input=b'last input\r', env=env)
        with open(history_file, 'rb') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), history_size)
        self.assertEqual(lines[-1].strip(), b'last input')
