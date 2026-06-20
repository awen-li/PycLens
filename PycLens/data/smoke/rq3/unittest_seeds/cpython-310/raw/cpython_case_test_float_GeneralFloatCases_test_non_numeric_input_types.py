# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_non_numeric_input_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CustomStr(str):
        pass

    class CustomBytes(bytes):
        pass

    class CustomByteArray(bytearray):
        pass
    factories = [bytes, bytearray, lambda b: CustomStr(b.decode()), CustomBytes, CustomByteArray, memoryview]
    try:
        from array import array
    except ImportError:
        pass
    else:
        factories.append(lambda b: array('B', b))
    for f in factories:
        x = f(b' 3.14  ')
        with self.subTest(type(x)):
            self.assertEqual(float(x), 3.14)
            with self.assertRaisesRegex(ValueError, 'could not convert'):
                float(f(b'A' * 16))
