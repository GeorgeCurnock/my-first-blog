from django.urls import reverse, resolve
from selenium import webdriver
import time

import unittest

from selenium.webdriver.common.keys import Keys


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
        # He notices the page title is referring to Bridging coursework
        self.assertIn('Bridging Coursework', self.browser.title)

        # He notices that on the right portion of the screen there are 2 headers 'blog' and 'cv'
        navbar_blog = self.browser.find_element_by_id('nav-blog').text
        self.assertIn('Blog', navbar_blog)
        navbar_cv = self.browser.find_element_by_id('nav-cv').text
        self.assertIn('CV', navbar_cv)

        # He clicks on the 'cv' header to take him to the cv portion of the web app
        self.browser.get('http://localhost:8000/cv/')
        # He notices the page title is referring to Bridging coursework

        # He is presented with a page containing a number of different headers and buttons referring to different
        # sections of a standard CV

        # He sees the heading of the first section is 'Basic Information'
        header_basic = self.browser.find_element_by_id('header_basic_information').text
        self.assertIn('Basic Information', header_basic)

        # James presses the 'Edit Basic Information' button
        edit_basic_button = self.browser.find_element_by_id('edit_basic_information').text
        self.assertIn('Add new Education entry', edit_basic_button)

        self.browser.get('http://localhost:8000/cv/edit/basic')

        # James is presented with a large header at the top of the page saying 'Basic Information' as well as
        # a number of subheaders each above a text field.
        '''
                 Different Sections for the basic information portion of the CV
                 Full name
                 Email address
                 Phone number
                 Github Link
                 LinkedIn Link
        '''

        edit_basic_header = self.browser.find_element_by_id('edit_basic_header').text
        self.assertIn('Basic Information', edit_basic_header)

        # He reads a sub header titled Full name
        edit_basic_name = self.browser.find_element_by_id('edit_basic_name').text
        self.assertIn('Full Name', edit_basic_name)

        # James enters his name into the text field
        edit_basic_name_field = self.browser.find_element_by_id('edit_basic_name_field')
        edit_basic_name_field.send_keys('James Semaj')

        # He reads a sub header titled Email
        edit_basic_email = self.browser.find_element_by_id('edit_basic_email').text
        self.assertIn('Email', edit_basic_email)

        # James enters his email into the text field
        edit_basic_email_field = self.browser.find_element_by_id('edit_basic_email_field')
        edit_basic_email_field.send_keys('james.semaj@gmail.com')

        # He reads a sub header titled Phone number
        edit_basic_phone = self.browser.find_element_by_id('edit_basic_phone').text
        self.assertIn('Phone Number', edit_basic_phone)

        # James enters his phone number into the text field
        edit_basic_phone_field = self.browser.find_element_by_id('edit_basic_phone_field')
        edit_basic_phone_field.send_keys('07759123456')

        # He reads a sub header titled Github Username
        edit_basic_github = self.browser.find_element_by_id('edit_basic_github').text
        self.assertIn('Github Username', edit_basic_github)

        # James enters his username into the text field
        edit_basic_github_field = self.browser.find_element_by_id('edit_basic_github_field')
        edit_basic_github_field.send_keys('CoderJames')

        # He reads a sub header titled LinkedIn Username
        edit_basic_linkedin = self.browser.find_element_by_id('edit_basic_linkedin').text
        self.assertIn('LinkedIn Username', edit_basic_linkedin)

        # James enters his username into the text field
        edit_basic_linkedin_field = self.browser.find_element_by_id('edit_basic_linkedin_field')
        edit_basic_linkedin_field.send_keys('James_Samaj')

        # He presses a button at the bottom of the page that says 'Save'
        edit_basic_save = self.browser.find_element_by_id('edit_basic_save').text
        self.assertIn('Save', edit_basic_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        self.browser.get('http://localhost:8000/cv/')
        # TODO write test to check that the information previously entered is being displayed

        # He sees a header "Education" with an option to 'add a new education entry'

        # He sees the heading of a section is 'Education'
        header_education = self.browser.find_element_by_id('header_education').text
        self.assertIn('Education', header_education)

        # James presses the 'Add a new education entry' button
        edit_education_button = self.browser.find_element_by_id('edit_education_button').text
        self.assertIn('Add new Education entry', edit_education_button)

        # He clicks the option
        self.browser.get('http://localhost:8000/cv/edit/education')

        # He is presented with a header titled 'Education Information'
        edit_education_header = self.browser.find_element_by_id('edit_basic_header').text
        self.assertIn('Education Information', edit_education_header)

        # He is presented with a number of sub headers and textfields
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

        # He reads a sub header titled Qualification
        edit_education_qualification = self.browser.find_element_by_id('edit_education_qualification').text
        self.assertIn('Qualification', edit_education_qualification)

        # James enters his qualification into the text field
        edit_education_qualification_field = self.browser.find_element_by_id('edit_education_qualification_field')
        edit_education_qualification_field.send_keys('MSci Computer Science')

        # He reads a sub header titled Period of Study
        edit_education_period = self.browser.find_element_by_id('edit_education_period').text
        self.assertIn('Period of Study', edit_education_period)

        # James enters the period of study into the text field
        edit_education_qualification_field = self.browser.find_element_by_id('edit_education_period_field')
        edit_education_qualification_field.send_keys('2017 - Present')

        # He reads a sub header titled Institution
        edit_education_institution = self.browser.find_element_by_id('edit_education_institution').text
        self.assertIn('Institution', edit_education_institution)

        # James enters the institution for the qualification into the text field
        edit_education_institution_field = self.browser.find_element_by_id('edit_institution_period_field')
        edit_education_institution_field.send_keys('University of Birmingham')

        # He reads a sub header Classification/Grade
        edit_education_grade = self.browser.find_element_by_id('edit_education_grade').text
        self.assertIn('Classification/Grade', edit_education_grade)

        # James enters the classification into the text field
        edit_education_grade_field = self.browser.find_element_by_id('edit_education_grade_field')
        edit_education_grade_field.send_keys('First Class')

        # He reads a sub header titled Brief Description of study
        edit_education_description = self.browser.find_element_by_id('edit_education_description').text
        self.assertIn('Description of study', edit_education_description)

        # James enters the period of study into the text field
        edit_education_description_field = self.browser.find_element_by_id('edit_education_description_field')
        edit_education_description_field.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting "
                                                   "industry. Lorem Ipsum has been the industry's standard dummy text "
                                                   "ever since the 1500s, when an unknown printer took a galley of "
                                                   "type and scrambled it to make a type specimen book. It has "
                                                   "survived not only five centuries, but also the leap into "
                                                   "electronic typesetting, remaining essentially unchanged. It was "
                                                   "popularised in the 1960s with the release of Letraset sheets "
                                                   "containing Lorem Ipsum passages, and more recently with desktop "
                                                   "publishing software like Aldus PageMaker including versions of "
                                                   "Lorem Ipsum.")

        # He presses a button at the bottom of the page that says 'Save'
        edit_education_save = self.browser.find_element_by_id('edit_education_save').text
        self.assertIn('Save', edit_education_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        self.browser.get('http://localhost:8000/cv/')
        # TODO write test to check that the information previously entered is being displayed

        # He is presented with a header titled 'Experience Information'
        header_experience = self.browser.find_element_by_id('header_experience').text
        self.assertIn('Experience Information', header_experience)

        # James presses the 'Add new experience entry' button
        edit_experience_button = self.browser.find_element_by_id('edit_experience_button').text
        self.assertIn('Add new Experience entry', edit_experience_button)

        self.browser.get('http://localhost:8000/cv/edit/experience')

        # He is presented with a number of sub headers and text fields
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

        # He reads a sub header titled Job Title
        edit_experience_title = self.browser.find_element_by_id('edit_experience_title').text
        self.assertIn('Job Title', edit_experience_title)

        # James enters his job title into the text field
        edit_experience_title_field = self.browser.find_element_by_id('edit_experience_title_field')
        edit_experience_title_field.send_keys('CEO')

        # He reads a sub header titled Period of Employment
        edit_experience_period = self.browser.find_element_by_id('edit_experience_period').text
        self.assertIn('Period of employment', edit_experience_period)

        # James enters his period of employment into the text field
        edit_experience_period_field = self.browser.find_element_by_id('edit_experience_period_field')
        edit_experience_period_field.send_keys('2015 - Present')

        # He reads a sub header titled Institution/Company
        edit_experience_company = self.browser.find_element_by_id('edit_experience_company').text
        self.assertIn('Institution/Company', edit_experience_company)

        # James enters his Institution/Company into the text field
        edit_experience_company_field = self.browser.find_element_by_id('edit_experience_company_field')
        edit_experience_company_field.send_keys('Google')

        # He reads a sub header titled Description of Work
        edit_experience_description = self.browser.find_element_by_id('edit_experience_description').text
        self.assertIn('Description of Work', edit_experience_description)

        # James enters his Institution/Company into the text field
        edit_experience_description_field = self.browser.find_element_by_id('edit_experience_description_field')
        edit_experience_description_field.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting "
                                                    "industry. Lorem Ipsum has been the industry's standard dummy text "
                                                    "ever since the 1500s, when an unknown printer took a galley of "
                                                    "type and scrambled it to make a type specimen book. It has "
                                                    "survived not only five centuries, but also the leap into "
                                                    "electronic typesetting, remaining essentially unchanged. It was "
                                                    "popularised in the 1960s with the release of Letraset sheets "
                                                    "containing Lorem Ipsum passages, and more recently with desktop "
                                                    "publishing software like Aldus PageMaker including versions of "
                                                    "Lorem Ipsum.")

        # He presses a button at the bottom of the page that says 'Save'
        edit_experience_save = self.browser.find_element_by_id('edit_experience_save').text
        self.assertIn('Save', edit_experience_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        self.browser.get('http://localhost:8000/cv/')
        # TODO write test to check that the information previously entered is being displayed

        # He sees a header "Projects" with an option to 'add a new project'

        # He is presented with a header titled 'Projects'
        header_project = self.browser.find_element_by_id('header_project').text
        self.assertIn('Project', header_project)

        # James presses the 'Add new experience entry' button
        edit_project_button = self.browser.find_element_by_id('edit_project_button').text
        self.assertIn('Add new Project', edit_project_button)

        # He clicks the option
        self.browser.get('http://localhost:8000/cv/edit/project')

        # He is presented with a header titled 'Projects' with a number of subheaders and textfields
        edit_project_header = self.browser.find_element_by_id('edit_project_header').text
        self.assertIn('Projects', edit_project_header)

        # He reads a sub header titled Project name
        edit_project_name = self.browser.find_element_by_id('edit_project_name').text
        self.assertIn('Project Name', edit_project_name)

        # James enters a project name into the text field
        edit_project_name_field = self.browser.find_element_by_id('edit_project_name_field')
        edit_project_name_field.send_keys('Orderly')

        # He reads a sub header titled Project technologies
        edit_project_technologies = self.browser.find_element_by_id('edit_project_technologies').text
        self.assertIn('Technologies', edit_project_technologies)

        # James types in a technology used for the project
        edit_project_technologies_field = self.browser.find_element_by_id('edit_project_technologies_field')
        edit_project_technologies_field.send_keys('HTML')

        # James presses enter to confirm the technology
        edit_project_technologies_field.send_keys(Keys.ENTER)

        # James can now see that the technology has been added to a list on the screen
        # TODO write check that list contains elements HTML and CSS

        # James types in another technology used for the project
        edit_project_technologies_field.send_keys('CSS')

        # James presses enter again to confirm the technology
        edit_project_technologies_field.send_keys(Keys.ENTER)

        # James can see that again the technology has been added to the list
        # TODO write check that list contains elements HTML and CSS

        # He reads a sub header titled Project description
        edit_project_description = self.browser.find_element_by_id('edit_project_description').text
        self.assertIn('Description', edit_project_description)

        # James types in a technology used for the project
        edit_project_description_field = self.browser.find_element_by_id('edit_project_description_field')
        edit_project_description_field.send_keys('HTML')

        # He presses a button at the bottom of the page that says 'Save'
        edit_project_save = self.browser.find_element_by_id('edit_project_save').text
        self.assertIn('Save', edit_project_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        self.browser.get('http://localhost:8000/cv/')
        # TODO write test to check that the information previously entered is being displayed

        # He is presented with a header titled 'Skills and Technologies' with an option to add a new skill/technology
        header_skill = self.browser.find_element_by_id('header_skills').text
        self.assertIn('Skills and Technologies', header_skill)

        edit_skill_button = self.browser.find_element_by_id('edit_skills_button').text
        self.assertIn('Add new Skill/Technology', edit_skill_button)

        # He clicks the option
        self.browser.get('http://localhost:8000/cv/edit/skills')

        # He reads a sub header titled Skill name
        edit_skill = self.browser.find_element_by_id('edit_skill').text
        self.assertIn('Skill', edit_skill)

        # James enters a project name into the text field
        edit_skill_field = self.browser.find_element_by_id('edit_skill_field')
        edit_skill_field.send_keys('HTML')

        # He presses a button at the bottom of the page that says 'Save'
        edit_skill_save = self.browser.find_element_by_id('edit_skill_save').text
        self.assertIn('Save', edit_skill_save)

        # TODO TESTS HAVE BEEN UNIT TESTED AND RAN UP TO THIS POINT
        self.fail("Tests have been completed up to this point")


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
