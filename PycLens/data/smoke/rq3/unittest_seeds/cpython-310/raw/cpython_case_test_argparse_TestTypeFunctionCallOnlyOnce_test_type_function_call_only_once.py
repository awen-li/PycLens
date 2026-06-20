# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestTypeFunctionCallOnlyOnce_test_type_function_call_only_once

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(string_to_convert):
        self.assertEqual(string_to_convert, 'spam!')
        return 'foo_converted'
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=spam, default='bar')
    args = parser.parse_args('--foo spam!'.split())
    self.assertEqual(NS(foo='foo_converted'), args)
