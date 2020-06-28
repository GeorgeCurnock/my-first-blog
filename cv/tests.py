from django.test import TestCase
from django.urls import reverse, resolve

from cv.models import Basic


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


class CVEditBasicPageTest(TestCase):

    def test_cv_basic_uses_cv_template(self):
        response = self.client.get(reverse('cv_edit_basic'))
        self.assertTemplateUsed(response, 'cv/cv_edit_basic.html')

    def test_can_save_basic_information_request(self):
        self.client.post(reverse('cv_edit_basic'), data=
        {'name': 'George Curnock', 'email': 'george.curnock@gmail.com',
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock'})

        self.assertEqual(Basic.objects.count(), 1)
        basic_info = Basic.objects.first()
        self.assertEqual(basic_info.text, {'name': 'George Curnock', 'email': 'george.curnock@gmail.com',
         'phone': '07759123456', 'github': 'GCurnock', 'linkedin': 'GeorgeCurnock'})

    def test_post_request_basic_information_redirects_to_cv_page(self):
        pass

    def test_only_saves_basic_information_content_when_necessary(self):
        pass

    def test_displays_all_basic_information_content(self):
        pass


class CVEditEducationInformationPageTest(TestCase):

    def test_can_save_education_information_post_request(self):
        pass

    def test_post_request_education_information_redirects_to_cv_page(self):
        pass

    def test_only_saves_education_information_items_when_necessary(self):
        pass

    def test_displays_all_education_information_items(self):
        pass


class CVEditExperienceInformationPageTest(TestCase):

    def test_post_request_experience_information_redirects_to_cv_page(self):
        pass

    def test_only_saves_experience_information_items_when_necessary(self):
        pass

    def test_displays_all_experience_information_items(self):
        pass


class CVEditProjectsInformationPageTest(TestCase):

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
