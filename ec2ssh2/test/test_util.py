import unittest
from ec2ssh2.util import ConstantDict, AttrDict

class TestConstantDict(unittest.TestCase):
    def test_func_val(self):
        data = ConstantDict(something=lambda: 'fish')
        self.assertEqual('fish', data['something'])

    def test_builtin_immutable(self):
        key_vals = dict(
            an_int=5,
            a_float=7.3,
            a_string='cats'
        )
        data = ConstantDict(**key_vals)
        for key, expected in key_vals.items():
            self.assertEqual(expected, data[key])

    def test_copied(self):
        data = ConstantDict(
            a_dict={'x': 10},
            an_array=[1, 2, 3]
        )
        dict1 = data['a_dict']
        self.assertEqual({'x': 10}, dict1)
        dict1['y'] = 17
        self.assertEqual({'x': 10}, data['a_dict'])
        array1 = data['an_array']
        self.assertEqual([1, 2, 3], array1)
        array1.append(4)
        self.assertEqual([1, 2, 3], data['an_array'])


class TestAttrDict(unittest.TestCase):
    def test_happy_1(self):
        data = AttrDict(key='value')
        self.assertEqual('value', data.key)

    def test_happy_2(self):
        data = AttrDict(key='value')
        self.assertEqual('value', data['key'])

    def test_sad_panda_1(self):
        data = AttrDict(key1='value')
        with self.assertRaises(AttributeError):
            unused = data.key2
            self.assertTrue(unused) # not reached

    def test_sad_panda_2(self):
        data = AttrDict(key1='value')
        with self.assertRaises(KeyError):
            unused = data['key2']
            self.assertTrue(unused) # not reached
