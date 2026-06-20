# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_changing_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    done = False

    class VeryActiveThread(threading.Thread):

        def run(self):
            with CreateKey(HKEY_CURRENT_USER, test_key_name) as key:
                use_short = True
                long_string = 'x' * 2000
                while not done:
                    s = 'x' if use_short else long_string
                    use_short = not use_short
                    SetValue(key, 'changing_value', REG_SZ, s)
    thread = VeryActiveThread()
    thread.start()
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name + '\\changing_value') as key:
            for _ in range(1000):
                (num_subkeys, num_values, t) = QueryInfoKey(key)
                for i in range(num_values):
                    name = EnumValue(key, i)
                    QueryValue(key, name[0])
    finally:
        done = True
        thread.join()
        DeleteKey(HKEY_CURRENT_USER, test_key_name + '\\changing_value')
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
