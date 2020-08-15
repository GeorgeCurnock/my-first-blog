from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_edit_and_view_the_cv(self):
        # James has been given access to the bridging coursework website as an admin in order to write blogs and have
        # a copy of his CV. He wants to check the website's CV section out to see what you can do

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
        self.assertIn('Edit Basic Information', edit_basic_button)

        self.browser.get('http://localhost:8000/cv/edit/basic')

        # James is presented with a large header at the top of the page saying 'Edit Basic Information' as well as
        # a fields each requiring data to be entered

        edit_basic_header = self.browser.find_element_by_id('edit_basic_header').text
        self.assertIn('Edit Basic Information', edit_basic_header)

        # He reads a sub header titled Full name
        edit_basic_name = self.browser.find_element_by_id('edit_basic_name').text
        self.assertIn('Full Name', edit_basic_name)

        # James enters his name into the text field
        edit_basic_name_field = self.browser.find_element_by_id('edit_basic_name_field')
        edit_basic_name_field.send_keys('James Chambers')

        # He reads a sub header titled Email address
        edit_basic_email = self.browser.find_element_by_id('edit_basic_email').text
        self.assertIn('Email Address', edit_basic_email)

        # James enters his email into the text field
        edit_basic_email_field = self.browser.find_element_by_id('edit_basic_email_field')
        edit_basic_email_field.send_keys('jamesChambers@gmail.com')

        # He reads a sub header titled Phone Number
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
        edit_basic_linkedin_field.send_keys('JamesChambers')

        # He has entered all the required information so presses a button at the bottom of the page that says 'Save'
        edit_basic_save = self.browser.find_element_by_id('edit_basic_save').text
        self.assertIn('Save', edit_basic_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        response = self.browser.get('http://localhost:8000/cv/')
        self.assertIn('James Chambers', response.content.decode())
        self.assertIn('jamesChambers@gmail.com', response.content.decode())
        self.assertIn('07759123456', response.content.decode())
        self.assertIn('CoderJames', response.content.decode())
        self.assertIn('JamesChambers', response.content.decode())

        # TODO Check that tests up to this point pass

        # He sees the heading of the next section is 'Education'
        education_header = self.browser.find_element_by_id('education_header').text
        self.assertIn('Education', education_header)

        # James presses the 'Add a new education entry' button
        edit_education_button = self.browser.find_element_by_id('edit_education_button').text
        self.assertIn('Add new Education entry', edit_education_button)

        # This sends him to a page to enter a new education entry
        self.browser.get('http://localhost:8000/cv/new/education')

        # He is presented with a header titled 'Add Education Entry' as well as fields each requiring data to be entered
        edit_education_header = self.browser.find_element_by_id('edit_education_header').text
        self.assertIn('Add Education Entry', edit_education_header)

        # James is presented with a large header at the top of the page saying 'Edit Basic Information' as well as
        # a fields each requiring data to be entered

        # He reads a sub header titled Qualification/Certification
        edit_education_qualification = self.browser.find_element_by_id('edit_education_qualification').text
        self.assertIn('Qualification/Certification', edit_education_qualification)

        # James enters his qualification into the text field
        edit_education_qualification_field = self.browser.find_element_by_id('edit_education_qualification_field')
        edit_education_qualification_field.send_keys('MSci Computer Science')

        # He reads a sub header titled Period of Study
        edit_education_period = self.browser.find_element_by_id('edit_education_period').text
        self.assertIn('Period of Study', edit_education_period)

        # James enters the period of study of which the qualification was completed into the text field
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

        # He reads a sub header titled Description of study
        edit_education_description = self.browser.find_element_by_id('edit_education_description').text
        self.assertIn('Description of study', edit_education_description)

        # James enters a description of the work he carried out whilst completing the qualification
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

        # He haas entered data into all the fields on the page so presses the save button at the bottom of the page
        edit_education_save = self.browser.find_element_by_id('edit_education_save').text
        self.assertIn('Save', edit_education_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        response = self.browser.get('http://localhost:8000/cv/')
        self.assertIn('MSci Computer Science', response.content.decode())
        self.assertIn('2017 - Present', response.content.decode())
        self.assertIn('University of Birmingham', response.content.decode())
        self.assertIn('First Class', response.content.decode())
        self.assertIn("Lorem Ipsum is simply dummy text of the printing and typesetting "
                      "industry. Lorem Ipsum has been the industry's standard dummy text "
                      "ever since the 1500s, when an unknown printer took a galley of "
                      "type and scrambled it to make a type specimen book. It has "
                      "survived not only five centuries, but also the leap into "
                      "electronic typesetting, remaining essentially unchanged. It was "
                      "popularised in the 1960s with the release of Letraset sheets "
                      "containing Lorem Ipsum passages, and more recently with desktop "
                      "publishing software like Aldus PageMaker including versions of "
                      "Lorem Ipsum.", response.content.decode())

        # TODO Check that tests up to this point pass

        # He is presented with a header titled 'Experience Information'
        header_experience = self.browser.find_element_by_id('header_experience').text
        self.assertIn('Experience', header_experience)

        # James presses the 'Add new experience entry' button
        edit_experience_button = self.browser.find_element_by_id('edit_experience_button').text
        self.assertIn('Add new Experience entry', edit_experience_button)

        self.browser.get('http://localhost:8000/cv/new/experience')

        # James is presented with a large header at the top of the page saying 'Edit Basic Information' as well as
        # a fields each requiring data to be entered
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
        edit_experience_title_field.send_keys('Software Developer Intern')

        # He reads a sub header titled Period of Employment
        edit_experience_period = self.browser.find_element_by_id('edit_experience_period').text
        self.assertIn('Period of Employment', edit_experience_period)

        # James enters his period of employment into the text field
        edit_experience_period_field = self.browser.find_element_by_id('edit_experience_period_field')
        edit_experience_period_field.send_keys('Summer 2018')

        # He reads a sub header titled Institution/Company
        edit_experience_company = self.browser.find_element_by_id('edit_experience_company').text
        self.assertIn('Institution/Company', edit_experience_company)

        # James enters his Institution/Company into the text field
        edit_experience_company_field = self.browser.find_element_by_id('edit_experience_company_field')
        edit_experience_company_field.send_keys('Google')

        # He reads a sub header titled Description of work
        edit_experience_description = self.browser.find_element_by_id('edit_experience_description').text
        self.assertIn('Description of work', edit_experience_description)

        # James enters a description of the work he carried tou  into the text field
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

        # He reads a sub header titled Referee
        edit_experience_referee = self.browser.find_element_by_id('edit_experience_referee').text
        self.assertIn('Referee', edit_experience_referee)

        # James enters a description of the work he carried tou  into the text field
        edit_experience_referee_field = self.browser.find_element_by_id('edit_experience_referee_field')
        edit_experience_referee_field.send_keys("Mark Oggle, 07759112233")

        # He presses a button at the bottom of the page that says 'Save'
        edit_experience_save = self.browser.find_element_by_id('edit_experience_save').text
        self.assertIn('Save', edit_experience_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        response = self.browser.get('http://localhost:8000/cv/')
        self.assertIn('Software Developer Intern', response.content.decode())
        self.assertIn('Summer 2018', response.content.decode())
        self.assertIn('Google', response.content.decode())
        self.assertIn('Mark Oggle, 07759112233', response.content.decode())
        self.assertIn("Lorem Ipsum is simply dummy text of the printing and typesetting "
                      "industry. Lorem Ipsum has been the industry's standard dummy text "
                      "ever since the 1500s, when an unknown printer took a galley of "
                      "type and scrambled it to make a type specimen book. It has "
                      "survived not only five centuries, but also the leap into "
                      "electronic typesetting, remaining essentially unchanged. It was "
                      "popularised in the 1960s with the release of Letraset sheets "
                      "containing Lorem Ipsum passages, and more recently with desktop "
                      "publishing software like Aldus PageMaker including versions of "
                      "Lorem Ipsum.", response.content.decode())

        # He sees a header "Projects" with an option to 'add a new project'
        # He is presented with a header titled 'Projects'
        header_project = self.browser.find_element_by_id('header_project').text
        self.assertIn('Projects', header_project)

        # James presses the 'Add new experience entry' button
        edit_project_button = self.browser.find_element_by_id('edit_project_button').text
        self.assertIn('Add new Project entry', edit_project_button)

        # He clicks the option
        self.browser.get('http://localhost:8000/cv/new/project')

        # James is presented with a large header at the top of the page saying 'Add a new project' as well as
        # a number of fields each requiring data to be entered
        edit_project_header = self.browser.find_element_by_id('edit_project_header').text
        self.assertIn('Add a Project', edit_project_header)

        # He reads a sub header titled Project name
        edit_project_name = self.browser.find_element_by_id('edit_project_name').text
        self.assertIn('Project Name', edit_project_name)

        # James enters a project name into the text field
        edit_project_name_field = self.browser.find_element_by_id('edit_project_name_field')
        edit_project_name_field.send_keys('Orderly')

        # He reads a sub header titled Project Description
        edit_project_description = self.browser.find_element_by_id('edit_project_description').text
        self.assertIn('Project Description', edit_project_description)

        # James enters a description of what the project is about
        edit_project_description_field = self.browser.find_element_by_id('edit_project_technologies_field')
        edit_project_description_field.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting "
                                                 "industry. Lorem Ipsum has been the industry's standard dummy text "
                                                 "ever since the 1500s, when an unknown printer took a galley of "
                                                 "type and scrambled it to make a type specimen book. It has "
                                                 "survived not only five centuries, but also the leap into "
                                                 "electronic typesetting, remaining essentially unchanged. It was "
                                                 "popularised in the 1960s with the release of Letraset sheets "
                                                 "containing Lorem Ipsum passages, and more recently with desktop "
                                                 "publishing software like Aldus PageMaker including versions of "
                                                 "Lorem Ipsum.")

        # He reads a sub header titled list of technologies used
        edit_project_technologies = self.browser.find_element_by_id('edit_project_description').text
        self.assertIn('List of technologies used', edit_project_technologies)

        # James enters a list of the different technologies involved in the project
        edit_project_technologies_field = self.browser.find_element_by_id('edit_project_technologies_field')
        edit_project_technologies_field.send_keys("HTML, CSS, DJANGO, Python, Javascript")

        # He presses a button at the bottom of the page that says 'Save'
        edit_project_save = self.browser.find_element_by_id('edit_project_save').text
        self.assertIn('Save', edit_project_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        response = self.browser.get('http://localhost:8000/cv/')
        self.assertIn('Orderly', response.content.decode())
        self.assertIn("Lorem Ipsum is simply dummy text of the printing and typesetting "
                      "industry. Lorem Ipsum has been the industry's standard dummy text "
                      "ever since the 1500s, when an unknown printer took a galley of "
                      "type and scrambled it to make a type specimen book. It has "
                      "survived not only five centuries, but also the leap into "
                      "electronic typesetting, remaining essentially unchanged. It was "
                      "popularised in the 1960s with the release of Letraset sheets "
                      "containing Lorem Ipsum passages, and more recently with desktop "
                      "publishing software like Aldus PageMaker including versions of "
                      "Lorem Ipsum.", response.content.decode())
        self.assertIn('HTML, CSS, DJANGO, Python, Javascript', response.content.decode())

        # He sees a header "Skills" with an option to 'add a new skill entry'
        header_skills = self.browser.find_element_by_id('header_skills').text
        self.assertIn('Skills', header_skills)

        edit_skill_button = self.browser.find_element_by_id('edit_skills_button').text
        self.assertIn('Add new Skill entry', edit_skill_button)

        # He clicks the option
        self.browser.get('http://localhost:8000/cv/new/skills')

        # He reads a sub header titled Skill name
        edit_skill = self.browser.find_element_by_id('edit_skill').text
        self.assertIn('Skill Name', edit_skill)

        # James enters the name of a skill he posses into the field
        edit_skill_field = self.browser.find_element_by_id('edit_skill_field')
        edit_skill_field.send_keys('HTML')

        # He presses a button at the bottom of the page that says 'Save'
        edit_skill_save = self.browser.find_element_by_id('edit_skill_save').text
        self.assertIn('Save', edit_skill_save)

        # He is returned to the cv page which has been updated to show the information he previously typed in
        response = self.browser.get('http://localhost:8000/cv/')
        self.assertIn('HTML', response.content.decode())

        # James decides that his description of work for the experience entry he entered doesnt describe what he did
        # as accurately as it could and decides he wants to edit it

        # James clicks the edit entry button next to the experience entry
        edit_experience_entry = self.browser.find_element_by_id("edit-experience-entry-1")
        edit_experience_entry.click()

        # James is returned the page where he first entered the experience information but this time each field already
        # contains the information he previously entered
        self.browser.get('http://localhost:8000/cv/edit/experience/1')

        edit_experience_title_field_text = self.browser.find_element_by_id('edit_experience_title_field').text
        self.assertEqual("Software Developer Intern", edit_experience_title_field_text)

        edit_experience_period_field_text = self.browser.find_element_by_id('edit_experience_period_field').text
        self.assertEqual("Summer 2018", edit_experience_period_field_text)

        edit_experience_company_field_text = self.browser.find_element_by_id('edit_experience_company_field').text
        self.assertEqual("Google", edit_experience_company_field_text)

        edit_experience_description_field_text = self.browser.find_element_by_id(
            'edit_experience_description_field').text
        self.assertEqual("Lorem Ipsum is simply dummy text of the printing and typesetting "
                         "industry. Lorem Ipsum has been the industry's standard dummy text "
                         "ever since the 1500s, when an unknown printer took a galley of "
                         "type and scrambled it to make a type specimen book. It has "
                         "survived not only five centuries, but also the leap into "
                         "electronic typesetting, remaining essentially unchanged. It was "
                         "popularised in the 1960s with the release of Letraset sheets "
                         "containing Lorem Ipsum passages, and more recently with desktop "
                         "publishing software like Aldus PageMaker including versions of "
                         "Lorem Ipsum.", edit_experience_description_field_text)

        edit_experience_referee_field_text = self.browser.find_element_by_id('edit_experience_referee_field').text
        self.assertEqual("Mark Oggle, 07759112233", edit_experience_referee_field_text)

        # James alters the description to make it more in line with the actual work he performed.
        edit_experience_description_field = self.browser.find_element_by_id('edit_experience_description_field')
        edit_experience_description_field.clear()
        edit_experience_description_field.send_keys("But I must explain to you how all this mistaken idea of "
                                                    "denouncing pleasure and praising pain was born and I will give "
                                                    "you a complete account of the system, and expound the actual "
                                                    "teachings of the great explorer of the truth, the master-builder "
                                                    "of human happiness. No one rejects, dislikes, or avoids pleasure "
                                                    "itself, because it is pleasure, but because those who do not "
                                                    "know how to pursue pleasure rationally encounter consequences "
                                                    "that are extremely painful. Nor again is there anyone who loves "
                                                    "or pursues or desires to obtain pain of itself, because it is "
                                                    "pain, but because occasionally circumstances occur in which toil "
                                                    "and pain can procure him some great pleasure. ")

        # He presses the save button to save the changes made
        response = self.browser.get('http://localhost:8000/cv/')
        # He is returned to the CV page where he sees that the description has in fact changed whilst all other data
        # remains the same
        self.assertIn('Software Developer Intern', response.content.decode())
        self.assertIn('Summer 2018', response.content.decode())
        self.assertIn('Google', response.content.decode())
        self.assertIn('Mark Oggle, 07759112233', response.content.decode())
        self.assertIn("But I must explain to you how all this mistaken idea of "
                      "denouncing pleasure and praising pain was born and I will give "
                      "you a complete account of the system, and expound the actual "
                      "teachings of the great explorer of the truth, the master-builder "
                      "of human happiness. No one rejects, dislikes, or avoids pleasure "
                      "itself, because it is pleasure, but because those who do not "
                      "know how to pursue pleasure rationally encounter consequences "
                      "that are extremely painful. Nor again is there anyone who loves "
                      "or pursues or desires to obtain pain of itself, because it is "
                      "pain, but because occasionally circumstances occur in which toil "
                      "and pain can procure him some great pleasure. ", response.content.decode())


if __name__ == '__main__':
    unittest.main(warnings='ignore')
