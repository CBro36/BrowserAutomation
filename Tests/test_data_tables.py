import unittest
from Tests.base_test import BaseTest
from Pages.data_tables_page import DataTablesPage
from Resources.locators import DataTablesLocators

class TestDataTables(BaseTest):
    def setUp(self):
        super().setUp()
        self.data_tables_page = DataTablesPage(self.driver)
        self.numCols = 6
        self.numRows = 4

    def testTable1(self):
        print("Table 1:")
        rows = self.data_tables_page.getRows(DataTablesLocators.Table1)
        
        #Gets the columns in each row, and prints each individual table entry
        for row in rows:
            cols = row.find_elements(*(DataTablesLocators.Tdata))
            for i in range(self.numCols):
                print(cols[i].text)

        #Verifies if the edit button is functional (The edit and delete buttons only changed the url,
        #they don't change the table in any way)
        self.data_tables_page.click(DataTablesLocators.EditButton)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/tables#edit')

    def testTable2(self):
        print("Table: 2")
        columns = [DataTablesLocators.LastNames, DataTablesLocators.FirstNames, DataTablesLocators.Emails, DataTablesLocators.Dues, DataTablesLocators.Sites]

        #For each column print each individual table entry, exlude column headers
        for col in columns:
            c = self.data_tables_page.getColumn(col)
            for i in range(1, self.numRows):
                print(c[i].text)

        #Verify functionality of delete button
        self.data_tables_page.click(DataTablesLocators.DeleteButton)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/tables#delete')

if __name__ == "__main__":
    unittest.main()