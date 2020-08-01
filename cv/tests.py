from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone

from cv.models import Basic, Education, Experience, Project, Skill


class CVHomeTest(TestCase):

    def test_cv_home_uses_cv_template(self):
        response = self.client.get(reverse('cv_home'))
        self.assertTemplateUsed(response, 'cv/cv_home.html')

    def test_edit_basic_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response,
                            '<a href="%s">Edit Basic Information</a>' % reverse("cv_edit_basic"),
                            html=True)

    def test_edit_basic_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/basic')
        self.assertEqual(resolver.view_name, 'cv_edit_basic')

    def test_edit_education_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response,
                            '<a href="%s">Add new Education entry</a>' % reverse("cv_edit_education"),
                            html=True)

    def test_edit_education_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/education')
        self.assertEqual(resolver.view_name, 'cv_edit_education')

    def test_edit_experience_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response,
                            '<a href="%s">Add new Experience entry</a>' % reverse("cv_edit_experience"),
                            html=True)

    def test_edit_experience_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/experience')
        self.assertEqual(resolver.view_name, 'cv_edit_experience')

    def test_edit_projects_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response, '<a href="%s">Add new Project</a>' % reverse("cv_edit_projects"),
                            html=True)

    def test_edit_projects_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/projects')
        self.assertEqual(resolver.view_name, 'cv_edit_projects')

    def test_edit_skills_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response, '<a href="%s">Add new Skill</a>' % reverse("cv_edit_skill"),
                            html=True)

    def test_edit_skills_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/skills')
        self.assertEqual(resolver.view_name, 'cv_edit_skills')


class CVBasicPageTest(TestCase):

    def test_cv_basic_uses_cv_template(self):
        response = self.client.get(reverse('cv_edit_basic'))
        self.assertTemplateUsed(response, 'cv/cv_edit_basic.html')

    def test_can_save_basic_request(self):
        self.client.post(reverse('cv_edit_basic'), data=
        {'name': 'George Curnock', 'email': 'george.curnock@gmail.com',
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock', 'last_updated': timezone.now()})

        self.assertEqual(Basic.objects.count(), 1)
        basic_info = Basic.objects.first()
        self.assertEqual(basic_info.name, 'George Curnock')
        self.assertEqual(basic_info.email, 'george.curnock@gmail.com')
        self.assertEqual(basic_info.phone, '07759123456')
        self.assertEqual(basic_info.github, 'GCurnock')
        self.assertEqual(basic_info.linkedin, 'GeorgeCurnock')

    def test_can_update_basic_request(self):
        self.client.post(reverse('cv_edit_basic'), data=
        {'name': 'George Curnock', 'email': 'george.curnock@gmail.com',
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock'})

        self.client.post(reverse('cv_edit_basic'), data=
        {'name': 'George Curnockey', 'email': 'george.curnock@sky.com',
         'phone': '077591234567', 'github': 'GCurnockey', 'linkedin': 'GeorgeCurnockey'})

        self.assertEqual(Basic.objects.count(), 1)
        basic_info = Basic.objects.first()
        self.assertEqual(basic_info.name, 'George Curnockey')
        self.assertEqual(basic_info.email, 'george.curnock@sky.com')
        self.assertEqual(basic_info.phone, '077591234567')
        self.assertEqual(basic_info.github, 'GCurnockey')
        self.assertEqual(basic_info.linkedin, 'GeorgeCurnockey')

    def test_post_request_basic_redirects_to_cv_page(self):
        response = self.client.post(reverse('cv_edit_basic'), data=
        {'name': 'George Curnock', 'email': 'george.curnock@gmail.com',
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')
        pass

    def test_displays_all_basic_information_content(self):
        self.client.post(reverse('cv_edit_basic'), data=
        {'name': 'George Curnock', 'email': 'george.curnock@gmail.com',
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock'})

        response = self.client.get(reverse('cv_home'))

        self.assertIn('George Curnock', response.content.decode())
        self.assertIn('george.curnock@gmail.com', response.content.decode())
        self.assertIn('07759123456', response.content.decode())
        self.assertIn('GCurnock', response.content.decode())
        self.assertIn('GeorgeCurnock', response.content.decode())


class CVNewEducationEntryTest(TestCase):

    def test_cv_new_education_uses_cv_template(self):
        response = self.client.get(reverse('cv_new_education'))
        self.assertTemplateUsed(response, 'cv/cv_edit_education.html')

    def test_can_save_experience_request(self):
        self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        self.assertEqual(Education.objects.count(), 1)
        education_info = Education.objects.first()
        self.assertEqual(education_info.qualification, 'MSci Computer Science')
        self.assertEqual(education_info.period, '2017 - Present')
        self.assertEqual(education_info.institution, 'University of Birmingham')
        self.assertEqual(education_info.grade, 'First Class')
        self.assertEqual(education_info.description,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                         'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                         'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                         'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                         'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                         )

    def test_post_request_education_redirects_to_cv_page(self):
        response = self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')
        pass

    def test_displays_all_education_information_content(self):
        self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        response = self.client.get(reverse('cv_home'))

        self.assertIn('MSci Computer Science', response.content.decode())
        self.assertIn('2017 - Present', response.content.decode())
        self.assertIn('University of Birmingham', response.content.decode())
        self.assertIn('First Class', response.content.decode())
        self.assertIn('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                      'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                      , response.content.decode())


class CVEditEducationEntryTest(TestCase):

    def test_cv_edit_education_uses_cv_template(self):
        self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        response = self.client.get(reverse('cv_edit_education', args=[1]))
        self.assertTemplateUsed(response, 'cv/cv_edit_education.html')

    def test_can_save_edited_education_request(self):
        self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        self.client.post(reverse('cv_edit_education', args=[1]), data=
        {'qualification': 'BSc Computer Science', 'period': '2017 - Present',
         'institution': 'Aston University', 'grade': '2:1',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        self.assertEqual(Education.objects.count(), 1)
        education_info = Education.objects.first()
        self.assertEqual(education_info.qualification, 'BSc Computer Science')
        self.assertEqual(education_info.period, '2017 - Present')
        self.assertEqual(education_info.institution, 'Aston University')
        self.assertEqual(education_info.grade, '2:1')
        self.assertEqual(education_info.description,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                         'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                         'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                         'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                         'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                         )

    def test_post_request_edit_education_redirects_to_cv_page(self):
        self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        response = self.client.post(reverse('cv_edit_education', args=[1]), data=
        {'qualification': 'BSc Computer Science', 'period': '2017 - Present',
         'institution': 'Aston University', 'grade': '2:1',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_displays_changed_education_information_content(self):
        self.client.post(reverse('cv_new_education'), data=
        {'qualification': 'MSci Computer Science', 'period': '2017 - Present',
         'institution': 'University of Birmingham', 'grade': 'First Class',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        self.client.post(reverse('cv_edit_education', args=[1]), data=
        {'qualification': 'BSc Computer Science', 'period': '2018 - Present',
         'institution': 'Aston University', 'grade': '2:1',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

        response = self.client.get(reverse('cv_home'))

        self.assertNotIn('MSci Computer Science', response.content.decode())
        self.assertNotIn('2017 - Present', response.content.decode())
        self.assertNotIn('University of Birmingham', response.content.decode())
        self.assertNotIn('First Class', response.content.decode())

        self.assertIn('BSc Computer Science', response.content.decode())
        self.assertIn('2018 - Present', response.content.decode())
        self.assertIn('Aston University', response.content.decode())
        self.assertIn('2:1', response.content.decode())
        self.assertIn('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                      'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                      , response.content.decode())


class CVNewExperienceEntryTest(TestCase):

    def test_cv_new_project_uses_cv_template(self):
        response = self.client.get(reverse('cv_new_project'))
        self.assertTemplateUsed(response, 'cv/cv_edit_project.html')

    def test_can_save_project_request(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'Orderly',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': ''})

        self.assertEqual(Experience.objects.count(), 1)
        experience_info = Experience.objects.first()
        self.assertEqual(experience_info.title, 'CEO')
        self.assertEqual(experience_info.period, '2019 - Present')
        self.assertEqual(experience_info.institution, 'Google')
        self.assertEqual(experience_info.referee, 'Sundar Pichai, 07759123457')
        self.assertEqual(experience_info.description,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                         'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                         'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                         'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                         'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                         )

    def test_post_request_experience_redirects_to_cv_page(self):
        response = self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')
        pass

    def test_displays_all_experience_information_content(self):
        self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})

        response = self.client.get(reverse('cv_home'))

        self.assertIn('CEO', response.content.decode())
        self.assertIn('2019 - Present', response.content.decode())
        self.assertIn('Google', response.content.decode())
        self.assertIn('Sundar Pichai, 07759123457', response.content.decode())
        self.assertIn('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                      'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                      , response.content.decode())


class CVEditExperienceEntryTest(TestCase):

    def test_cv_edit_experience_uses_cv_template(self):
        self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})

        response = self.client.get(reverse('cv_edit_experience', args=[1]))
        self.assertTemplateUsed(response, 'cv/cv_edit_experience.html')

    def test_can_save_edited_experience_request(self):
        self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})

        self.client.post(reverse('cv_edit_experience', args=[1]), data=
        {'title': 'Boss', 'period': '2020 - Present',
         'institution': 'SpaceX',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Elon Musk, 07759123456'})

        self.assertEqual(Experience.objects.count(), 1)
        experience_info = Experience.objects.first()
        self.assertEqual(experience_info.title, 'Boss')
        self.assertEqual(experience_info.period, '2020 - Present')
        self.assertEqual(experience_info.institution, 'SpaceX')
        self.assertEqual(experience_info.referee, 'Elon Musk, 07759123456')
        self.assertEqual(experience_info.description,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                         'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                         'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                         'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                         'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                         )

    def test_post_request_edit_experience_redirects_to_cv_page(self):
        self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})

        response = self.client.post(reverse('cv_edit_experience', args=[1]), data=
        {'title': 'Boss', 'period': '2020 - Present',
         'institution': 'SpaceX',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Elon Musk, 07759123456'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_displays_changed_experience_information_content(self):
        self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})

        self.client.post(reverse('cv_edit_experience', args=[1]), data=
        {'title': 'Boss', 'period': '2020 - Present',
         'institution': 'SpaceX',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Elon Musk, 07759123456'})

        response = self.client.get(reverse('cv_home'))

        self.assertNotIn('CEO', response.content.decode())
        self.assertNotIn('2019 - Present', response.content.decode())
        self.assertNotIn('Google', response.content.decode())
        self.assertNotIn('Sundar Pichai, 07759123457', response.content.decode())

        self.assertIn('Boss', response.content.decode())
        self.assertIn('2020 - Present', response.content.decode())
        self.assertIn('SpaceX', response.content.decode())
        self.assertIn('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                      'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                      , response.content.decode())
        self.assertIn('Elon Musk, 07759123456', response.content.decode())


class CVNewProjectsEntryTest(TestCase):

    def test_cv_new_project_uses_cv_template(self):
        response = self.client.get(reverse('cv_new_project'))
        self.assertTemplateUsed(response, 'cv/cv_edit_projects.html')

    def test_can_save_project_request(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})

        self.assertEqual(Project.objects.count(), 1)
        project_info = Project.objects.first()
        self.assertEqual(project_info.title, 'my-first-blog')
        self.assertEqual(project_info.description,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                         'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                         'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                         'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                         'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                         )
        self.assertEqual(project_info.technologies, 'HTML, CSS, JS, Python, DJango')

    def test_post_request_project_redirects_to_cv_page(self):
        response = self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_displays_all_project_information_content(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})

        response = self.client.get(reverse('cv_home'))

        self.assertIn('my-first-blog', response.content.decode())
        self.assertIn('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                      'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                      , response.content.decode())
        self.assertIn('HTML, CSS, JS, Python, DJango', response.content.decode())


class CVEditProjectEntryTest(TestCase):

    def test_cv_edit_project_uses_cv_template(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})

        response = self.client.get(reverse('cv_edit_project', args=[1]))
        self.assertTemplateUsed(response, 'cv/cv_edit_projects.html')

    def test_can_save_edited_project_request(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})

        self.client.post(reverse('cv_edit_project', args=[1]), data=
        {'title': 'Orderly',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, Golang'})

        self.assertEqual(Project.objects.count(), 1)
        project_info = Project.objects.first()
        self.assertEqual(project_info.title, 'Orderly')
        self.assertEqual(project_info.technologies, 'HTML, CSS, JS, Python, Golang')
        self.assertEqual(project_info.description,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                         'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                         'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                         'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                         'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                         )

    def test_post_request_edit_project_redirects_to_cv_page(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})

        response = self.client.post(reverse('cv_edit_project', args=[1]), data=
        {'title': 'Orderly',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, Golang'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_displays_changed_project_information_content(self):
        self.client.post(reverse('cv_new_project'), data=
        {'title': 'my-first-blog',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, DJango'})

        self.client.post(reverse('cv_edit_project', args=[1]), data=
        {'title': 'Orderly',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'technologies': 'HTML, CSS, JS, Python, Golang'})

        response = self.client.get(reverse('cv_home'))

        self.assertNotIn('my-first-blog', response.content.decode())
        self.assertNotIn('HTML, CSS, JS, Python, DJango', response.content.decode())

        self.assertIn('Orderly', response.content.decode())
        self.assertIn('HTML, CSS, JS, Python, Golang', response.content.decode())
        self.assertIn('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                      'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
                      , response.content.decode())


class CVNewSkillPageTest(TestCase):

    def test_cv_edit_skill_uses_cv_template(self):
        response = self.client.get(reverse('cv_new_skill'))
        self.assertTemplateUsed(response, 'cv/cv_edit_skills.html')

    def test_can_save_project_request(self):
        self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})
        self.assertEqual(Skill.objects.count(), 1)
        skill_info = Skill.objects.first()
        self.assertEqual(skill_info.name, 'HTML')

    def test_post_request_project_redirects_to_cv_page(self):
        response = self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_displays_all_project_information_content(self):
        self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})

        response = self.client.get(reverse('cv_home'))

        self.assertIn('HTML', response.content.decode())


class CVEditSkillPageTest(TestCase):

    def test_cv_edit_project_uses_cv_template(self):
        self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})

        response = self.client.get(reverse('cv_edit_skill', args=[1]))
        self.assertTemplateUsed(response, 'cv/cv_edit_skills.html')

    def test_can_save_edited_project_request(self):
        self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})

        self.client.post(reverse('cv_edit_skill', args=[1]), data=
        {'name': 'CSS'})

        self.assertEqual(Skill.objects.count(), 1)
        skill_info = Skill.objects.first()
        self.assertEqual(skill_info.name, 'CSS')

    def test_post_request_edit_project_redirects_to_cv_page(self):
        self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})

        response = self.client.post(reverse('cv_edit_skill', args=[1]), data=
        {'name': 'CSS'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_displays_changed_project_information_content(self):
        self.client.post(reverse('cv_new_skill'), data=
        {'name': 'HTML'})

        self.client.post(reverse('cv_edit_skill', args=[1]), data=
        {'name': 'CSS'})

        response = self.client.get(reverse('cv_home'))

        self.assertNotIn('HTML', response.content.decode())
        self.assertIn('CSS', response.content.decode())
