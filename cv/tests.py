from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse, resolve

from cv.models import Basic, Education, Experience


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
        self.assertContains(response, '<a href="%s">Add new Skill</a>' % reverse("cv_edit_skills"),
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
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock'})

        self.assertEqual(Basic.objects.count(), 1)
        basic_info = Basic.objects.first()
        self.assertEqual(basic_info.name, 'George Curnock')
        self.assertEqual(basic_info.email, 'george.curnock@gmail.com')
        self.assertEqual(basic_info.phone, '07759123456')
        self.assertEqual(basic_info.github, 'GCurnock')
        self.assertEqual(basic_info.linkedin, 'GeorgeCurnock')

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
    pass


class CVNewExperiencePageTest(TestCase):

    def test_cv_new_experience_uses_cv_template(self):
        response = self.client.get(reverse('cv_new_experience'))
        self.assertTemplateUsed(response, 'cv/cv_edit_experience.html')

    def test_can_save_experience_request(self):
        self.client.post(reverse('cv_new_experience'), data=
        {'title': 'CEO', 'period': '2019 - Present',
         'institution': 'Google',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
                        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
         'referee': 'Sundar Pichai, 07759123457'})

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


class CVEditProjectsPageTest(TestCase):

    def test_can_save_projects_information_post_request(self):
        pass

    def test_post_request_projects_information_redirects_to_cv_page(self):
        pass

    def test_only_saves_projects_information_items_when_necessary(self):
        pass

    def test_displays_all_projects_information_items(self):
        pass


class CVEditSkillsPageTest(TestCase):

    def test_can_save_skills_post_request(self):
        pass

    def test_post_request_skills_redirects_to_cv_page(self):
        pass

    def test_only_saves_skills_items_when_necessary(self):
        pass

    def test_displays_all_skills_items(self):
        pass
