from topicSwap import switchTopic, resetToStadartTopic

import unittest
import re
import os
class TestSwitchTopi(unittest.TestCase):
    def testNormalPattern(self):
        input = "hallo123"
        output = 'currentTopicChannelId = "hallo123"'
        switchTopic(input)
        print("kalkdölfkdsajfölsakdfölsakdjfsaölkfsalkdjsaadafasdfsaf")
        print(os.getcwd())
        with open("./src/variable.py", "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.fullmatch(output, line):
                    self.assertEqual(output, line)
                    resetToStadartTopic()
    def testNoPattern(self):
        input = ""
        output = 'currentTopicChannelId = ""'
        switchTopic(input)
        with open("./src/variable.py", "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.fullmatch(output, line):
                    self.assertEqual(output, line)
                    resetToStadartTopic()

class TestRestTopic(unittest.TestCase):
    def testNormalReset(self):
        output = 'currentTopicChannelId = "UCsd4OmYbE6BeYEdm-Vn7pcQ"'
        resetToStadartTopic()
        with open("./src/variable.py", "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.fullmatch(output, line):
                    self.assertEqual(output, line)


if __name__ == '__main__':
  unittest.main()