# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_user_defined_action

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Success(Exception):
        pass

    class Action(object):

        def __init__(self, option_strings, dest, const, default, required=False):
            if dest == 'spam':
                if const is Success:
                    if default is Success:
                        raise Success()

        def __call__(self, *args, **kwargs):
            pass
    parser = argparse.ArgumentParser()
    self.assertRaises(Success, parser.add_argument, '--spam', action=Action, default=Success, const=Success)
    self.assertRaises(Success, parser.add_argument, 'spam', action=Action, default=Success, const=Success)
