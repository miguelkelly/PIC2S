#! /usr/bin/env python
"""
    test_FileReader
    Test suite for FileReader module
"""
import unittest
import FileReader
import os

class test_FileReader(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_filenames(self):

        # verify that a list is returned
        self.assertTrue(isinstance(FileReader.getFileNames('*'),list))
        # verify that the list is long enough
        filenames = FileReader.getFileNames('*')
        self.assertTrue(len(filenames) > 0)
        # verify that the list don't contain directorys
        for filename in filenames:
            self.assertFalse(os.path.isdir(filename))


if __name__ == "__main__":
    unittest.main()
