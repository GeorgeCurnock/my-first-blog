from selenium import webdriver

import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_edit_view_print_and_download_the_cv(self):
        self.fail("Finish the test!")

        # James has been given access to the bridging coursework website as an admin in order to write blogs and have
        # a copy of his CV. He wants to check the website out to see what you can do

        # He goes to the web address of the homepage of the website

        # He notices that on the right portion of the screen there are 2 headers 'blog' and 'cv'

        # He clicks on the 'cv' header to see where it takes him

        # He is presented with a page that a number of different headers and buttons
        # He clicks on the edit button next to the 'basic information' header

        # James is presented with a number of text fields each with their own headers

        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He is returned to the cv page which has been updated to show the information he previously typed in

        # He sees a header "Education" with an option to 'add a new education'
        # He clicks the option

        # He is presented with a number of different text fields regarding ones education
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He is returned to the cv page where, once again, the page has been updated with the newly entered information

        # He sees a header "Projects" with an option to 'add a new project'
        # He clicks the option

        # He is presented with a number of different text fields regarding ones education
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He sees a header "Interests" with an option to 'add a new interest'
        # He clicks the option

        # He is presented with a number of different text fields regarding ones education
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He sees a header "Technologies" with an option to add a new technology"
        # He clicks the option

        # He is presented with a text field to enter a technology and a slider with different names to represent his
        # efficiency in that technology
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He sees a button at the bottom of the page to print
        # He clicks this button and is presented with a print page of his entered CV

        # He sees a button at the bottom of the page to download
        # He clicks this button and a file starts to download containing his entered CV information


if __name__ == '__main__':
    unittest.main(warnings='ignore')
