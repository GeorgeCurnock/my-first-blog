from django.test import TestCase
from django.urls import reverse, resolve


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

    def test_edit_technologies_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response, '<a href="%s">Add new Technology</a>' % reverse("cv_edit_technologies"),
                            html=True)

    def test_edit_technologies_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/technologies')
        self.assertEqual(resolver.view_name, 'cv_edit_technologies')

    def test_edit_other_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response, '<a href="%s">Edit Other Interests</a>' % reverse("cv_edit_other"),
                            html=True)

    def test_edit_other_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/other')
        self.assertEqual(resolver.view_name, 'cv_edit_other')


class CVEditBasicPageTest(TestCase):

    def test_cv_home_uses_cv_template(self):
        response = self.client.get(reverse('cv_edit_basic'))
        self.assertTemplateUsed(response, 'cv/cv_basic.html')

    def test_can_save_basic_information_request(self):
        self.client.post(reverse('cv_basic'), data={})

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


class CVEditTechnologiesPageTest(TestCase):

    def test_can_save_technologies_post_request(self):
        pass

    def test_post_request_technologies_redirects_to_cv_page(self):
        pass

    def test_only_saves_technologies_items_when_necessary(self):
        pass

    def test_displays_all_technolgies_items(self):
        pass


class CVEditOtherPageTest(TestCase):

    def test_can_save_other_post_request(self):
        pass

    def test_post_request_other_redirects_to_cv_page(self):
        pass

    def test_only_saves_other_items_when_necessary(self):
        pass

    def test_displays_all_other_items(self):
        pass
