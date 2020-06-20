from django.urls import reverse
from selenium import webdriver
import time

import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_edit_view_print_and_download_the_cv(self):
        # James has been given access to the bridging coursework website as an admin in order to write blogs and have
        # a copy of his CV. He wants to check the website out to see what you can do

        # He goes to the web address of the homepage of the website
        self.browser.get('http://localhost:8000')
        time.sleep(15)
        # He notices the page title is referring to Bridging coursework
        self.assertIn('Bridging Coursework', self.browser.title)



        # He notices that on the right portion of the screen there are 2 headers 'blog' and 'cv'
        navbar_blog = self.browser.find_element_by_id('nav-blog').text
        self.assertIn('Blog', navbar_blog)
        navbar_cv = self.browser.find_element_by_id('nav-cv').text
        self.assertIn('CV', navbar_cv)

        # He clicks on the 'cv' header to take him to the cv portion of the web app
        navbar_blog_location = self.browser.get(reverse("/"))
        self.assertIn(navbar_blog_location, '<a href="%s">CV</a>' % reverse("/cv"))

        # He is presented with a page containing a number of different headers and buttons referring to different
        # sections of a standard CV

        # He sees the heading of the first section is 'Basic Information'
        basic_information_heading = self.browser.find_element_by_id('header-basic-information').text
        self.assertIn('Basic Information', basic_information_heading)

        # He clicks on the edit button next to the 'basic information' header
        edit_basic_information_button_location = self.browser.get(reverse("/cv"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(edit_basic_information_button_location,
                      '<a href="%s">Edit</a>' % reverse("/cv/edit/basic-information"))

        # James is presented with a number of text fields each with their own headers
        '''
         Different Sections for the basic information portion of the CV
         Full name
         Email address
         Phone number
         Github Link
         LinkedIn Link
        '''
        # He fills out the text fields with the required information and presses the save button
        # TODO write checks that each header listed above exists
        # TODO write checks that you can enter information into each text field

        # He is returned to the cv page which has been updated to show the information he previously typed in
        save_basic_information_button_location = self.browser.get(reverse("/cv/edit/basic-information"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(save_basic_information_button_location,
                      '<a href="%s"Save</a>' % reverse("/cv"))

        # He sees a header "Education" with an option to 'add a new education'
        # He clicks the option
        edit_education_information_button_location = self.browser.get(reverse("/cv"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(edit_education_information_button_location,
                      '<a href="%s">Edit</a>' % reverse("/cv/edit/education-information"))

        # He is presented with a number of different text fields regarding ones education
        # He fills out the text fields with the required information and presses the save button
        '''
        Lists the different forms of education currently saved
        Option to add a new education entry
        
        # Education entry consists of
            Qualification
            Period of study
            Institution
            Classification/Grade
            Description of work completed
        '''
        # TODO write a check that there's a button to add a new education entry
        # TODO write a check that you can save a new entry

        # James decides to add a new education entry to his CV
        # TODO complete this test

        # He clicks the save button and is returned to the cv page where, once again,
        # the page has been updated with the newly entered information
        save_education_information_button_location = self.browser.get(reverse("/cv/edit/education-information"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(save_education_information_button_location,
                      '<a href="%s"Save</a>' % reverse("/cv"))

        # He sees a header "Experience" with an option to 'add new experience'
        # He clicks the option
        edit_experience_information_button_location = self.browser.get(reverse("/cv"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(edit_experience_information_button_location,
                      '<a href="%s">Edit</a>' % reverse("/cv/edit/experience-information"))

        # He is presented with a number of different text fields regarding ones education
        # He fills out the text fields with the required information and presses the save button
        '''
        Lists the different experiences currently saved
        Option to add a new experience entry
        
        # Experience entry consists of
            Job title
            Period of employment
            Institution/Company
            Description of work undertaken
            Potential referee
        '''

        # TODO write a check that there's a button to add a new experience entry
        # TODO write a check that you can save a new entry

        # James decides to add a new experience entry to his CV
        # TODO complete this test

        # He clicks the save button and is returned to the cv page where, once again,
        # the page has been updated with the newly entered information
        save_experience_information_button_location = self.browser.get(reverse("/cv/edit/experience-information"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(save_experience_information_button_location,
                      '<a href="%s"Save</a>' % reverse("/cv"))

        # He sees a header "Projects" with an option to 'add a new project'
        # He clicks the option
        edit_project_information_button_location = self.browser.get(reverse("/cv"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(edit_project_information_button_location,
                      '<a href="%s">Edit</a>' % reverse("/cv/edit/project-information"))

        # He is presented with a number of different text fields regarding projects
        '''
        # A project will have a number of generic fields to give those who read it enough information to be interested about it
            Project title
            project technologies
            brief project description
            
        '''
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He clicks the save button and is returned to the cv page where, once again,
        # the page has been updated with the newly entered information
        save_project_information_button_location = self.browser.get(reverse("/cv/edit/project-information"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(save_project_information_button_location,
                      '<a href="%s"Save</a>' % reverse("/cv"))



        # TODO Determine a good format for the following sections and if they are needed
'''
        # He sees a header "Interests" with an option to 'add a new interest'
        # He clicks the option
        edit_interests_button_location = self.browser.get(reverse("/cv"))
        # TODO Ensure the icon and text contained in the link is correct
        self.assertIn(edit_interests_button_location,
                      '<a href="%s">Edit</a>' % reverse("/cv/edit/interests"))

        # He is presented with a number of different text fields regarding ones interests
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He sees a header "Technologies" with an option to add a new technology"
        # He clicks the option
        edit_basic_button_location = self.browser.find_element_by_id('edit-basic-information-button').location
        self.assertIn('#', edit_basic_button_location)

        # He is presented with a text field to enter a technology and a slider with different names to represent his
        # efficiency in that technology
        # He fills out the text fields with the required information and presses the save button
        # TODO Make this more specific

        # He sees a button at the bottom of the page to print
        # He clicks this button and is presented with a print page of his entered CV

        # He sees a button at the bottom of the page to download
        # He clicks this button and a file starts to download containing his entered CV information

'''

if __name__ == '__main__':
    unittest.main(warnings='ignore')
