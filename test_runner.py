import unittest
from HTMLTestRunner import HTMLTestRunner
from tests.test_data_cleanup import TestDataCleanup
from tests.test_data_processing import TestDataProcessing
from tests.test_data_grouping import TestDataGrouping
from tests.test_data_temporal_analysis import TestDataTemporalAnalysis
from tests.test_data_status_analysis import TestDataStatusAnalysis

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    suite = unittest.TestSuite()

    # Guardamos los casos de los test.
    test_suite_data_cleanup = unittest.TestLoader().loadTestsFromTestCase(TestDataCleanup)
    test_suite_data_processing = unittest.TestLoader().loadTestsFromTestCase(TestDataProcessing)
    test_suite_data_grouping = unittest.TestLoader().loadTestsFromTestCase(TestDataGrouping)
    test_suite_data_temporal_analysis = unittest.TestLoader().loadTestsFromTestCase(TestDataTemporalAnalysis)
    test_suite_data_status_analysis = unittest.TestLoader().loadTestsFromTestCase(TestDataStatusAnalysis)

    # Los agrupamos en suites o casos.
    suite.addTest(test_suite_data_cleanup)
    suite.addTest(test_suite_data_processing)
    suite.addTest(test_suite_data_grouping)
    suite.addTest(test_suite_data_temporal_analysis)
    suite.addTest(test_suite_data_status_analysis)

    # Agregamos la localización y titulo.
    runner = HTMLTestRunner(output='reports', title="Reports")

    # Genera el reporte.
    runner.run(suite)
