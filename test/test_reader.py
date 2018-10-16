"""Tests for module funcs"""
from __future__ import absolute_import
import unittest
from libs.reader import Reader


class TestReaderFileOperation(unittest.TestCase):
    """Tests file opening and reading operations"""

    def test_r_with_no_file(self):
        """Tests def open_file(filename)"""
        R = Reader("")

        self.assertEqual(False, R.is_valid)
        self.assertEqual(None, R.sport)
        self.assertEqual(None, R.sport_id)

    def test_check_tcx(self):
        """Tests def check_tcx"""
        R = Reader("test/run-garmin.tcx")
        R.read()

        self.assertEqual(True, R.is_valid)
        self.assertEqual('Running', R.sport)
        self.assertEqual("2018-06-29T17:46:33.000Z", R.sport_id)
        self.assertEqual("Build Version: 18.16.7.7",
                         R.author.build.to_string())
        self.assertEqual("en", R.author.lang_id)
        self.assertEqual("006-D2449-00", R.author.part_number)
        self.assertEqual("Garmin Connect API", R.author.name)

        del R

        R = Reader("test/run-polar.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Running", R.sport)
        self.assertEqual("2018-08-04T04:26:43.000Z", R.sport_id)
        R.read()
        self.assertEqual("Build Version: 0.0", R.author.build.to_string())
        self.assertEqual("EN", R.author.lang_id)
        self.assertEqual("XXX-XXXXX-XX", R.author.part_number)
        self.assertEqual("Polar Flow Mobile Viewer", R.author.name)

        del R
        R = Reader("test/run-runtastic.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Running", R.sport)
        self.assertEqual("2018-06-20T16:40:35.000Z", R.sport_id)
        R.read()

        del R

        R = Reader("test/run-tapirik.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Running", R.sport)
        self.assertEqual("2018-06-03T03:13:35.000Z", R.sport_id)
        R.read()
        self.assertEqual("Build Version: 0.0.0.0", R.author.build.to_string())
        self.assertEqual("en", R.author.lang_id)
        self.assertEqual("000-00000-00", R.author.part_number)
        self.assertEqual("tapiriik", R.author.name)

        del R
        R = Reader("test/bike-garmin.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Cycling", R.sport)
        self.assertEqual("2018-06-16T04:12:47.000Z", R.sport_id)
        R.read()
        self.assertEqual("Build Version: 18.16.7.7",
                         R.author.build.to_string())
        self.assertEqual("en", R.author.lang_id)
        self.assertEqual("006-D2449-00", R.author.part_number)
        self.assertEqual("Garmin Connect API", R.author.name)

        del R

        R = Reader("test/bike-polar.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Cycling", R.sport)
        self.assertEqual("2017-07-31T16:03:39.000Z", R.sport_id)
        R.read()
        self.assertEqual("Build Version: 0.0", R.author.build.to_string())
        self.assertEqual("EN", R.author.lang_id)
        self.assertEqual("XXX-XXXXX-XX", R.author.part_number)
        self.assertEqual("Polar Flow Mobile Viewer", R.author.name)


        del R

        R = Reader("test/bike-runtastic.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Cycling", R.sport)
        self.assertEqual("2018-05-16T15:03:56.000Z", R.sport_id)
        R.read()
        
        del R

        R = Reader("test/bike-tapirik.tcx")
        self.assertEqual(True, R.is_valid)
        self.assertEqual("Cycling", R.sport)
        self.assertEqual("2018-06-16T04:12:47.000Z", R.sport_id)
        R.read()
        self.assertEqual("Build Version: 0.0.0.0", R.author.build.to_string())
        self.assertEqual("en", R.author.lang_id)
        self.assertEqual("000-00000-00", R.author.part_number)
        self.assertEqual("tapiriik", R.author.name)

        del R
        R = Reader("test/error.tcx")
        R.read()
        self.assertEqual(False, R.is_valid)
        self.assertEqual("mismatched tag: line 52, column 8\n", R.last_error)

        del R
        R = Reader("test/error.1.tcx")
        self.assertEqual(False, R.is_valid)
        self.assertEqual(
            "File \"test/error.1.tcx\" is not a valid TCX file\n", R.last_error)


if __name__ == '__main__':
    unittest.main()
