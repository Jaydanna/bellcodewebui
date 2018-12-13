#!/user/bin/env python3
#coding=utf-8


import unittest
from myfunction import HTMLTestRunner
from tests.test_video import TestVideo
from tests.test_puzzle2 import TestPuzzle2
import time


def main():

    suits=unittest.TestSuite()
    loader=unittest.TestLoader()
    # suits.addTests(loader.loadTestsFromTestCase(TestVideo))
    suits.addTests(loader.loadTestsFromTestCase(TestPuzzle2))

    return suits

def export_report():
    
    return testRunner

if __name__=="__main__":
    fp = open(r'../python/reports/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    testRunner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description="Report:")
    testRunner.run(main())