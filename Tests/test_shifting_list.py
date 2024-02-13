import unittest
from Tests.base_test import BaseTest
from Pages.shifting_list_page import ShiftingListPage

class TestShiftingList(BaseTest):
    def setUp(self):
        super().setUp()
        self.shift_list_page = ShiftingListPage(self.driver)

    def testList(self):
        li = self.shift_list_page.getLines()
        
        i = 1
        for line in li:
            line = line.strip()
            if line != "":
                line = line.removesuffix('<br><br>')
                #Finds and prints the correct line from the list
                if line == "Important Information You're Looking For":
                    print('Line ' + str(i) +  ': ' + line)
                i += 1

if __name__ == "__main__":
    unittest.main()