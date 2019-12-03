import unittest
import number
import elk


class TestNumber(unittest.TestCase):

    def test_is_prime_7(self):
        self.assertTrue( number.is_prime(7) )

    def test_is_prime_2(self):
        self.assertTrue( number.is_prime(2) )

    def test_is_prime_4(self):
        self.assertFalse( number.is_prime(4) )

class TestELK(unittest.TestCase):

    def test_simple(self):

        struct1 = {
            'one': 'blue',
            'two': 'red',
            'three': 'green'
        }

        docs = elk.dict_to_doc(struct1)
        self.assertEqual(len(docs),1)
        self.assertEqual(docs[0]['one'],'blue')
        self.assertEqual(docs[0]['two'],'red')
        self.assertEqual(docs[0]['three'],'green')


    def test_with_list(self):
        struct1 = {
            'one': 'blue',
            'two': ['red','rojo'],
            'three': 'green'
        }

        self.assertTrue(True)

    def test_with_dict(self):
        self.assertTrue(True)

    def test_complex(self):
        self.assertTrue(True)
