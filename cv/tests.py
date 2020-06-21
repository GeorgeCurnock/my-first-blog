from django.test import TestCase
from django.urls import reverse, resolve


class CVHomeTest(TestCase):

    def test_cv_home_uses_cv_template(self):
        response = self.client.get(reverse('cv_home'))
        self.assertTemplateUsed(response, 'cv/cv_home.html')

    def test_edit_basic_information_link_leads_to_correct_URL(self):
        response = self.client.get(reverse("cv_home"))
        self.assertContains(response, '<a href="%s">Edit Basic Information</a>' % reverse("edit_basic_information"),
                            html=True)

    def test_edit_basic_information_URL_uses_correct_view_function(self):
        resolver = resolve('/cv/edit/basic-information/')
        self.assertEqual(resolver.view_name, 'edit_basic_information')



    def test_can_access_edit_education_information_page(self):
        pass

    def test_can_access_edit_experience_information_page(self):
        pass

    def test_can_save_experience_information_post_request(self):
        pass

    def test_can_access_edit_projects_information_page(self):
        pass

    def test_can_access_edit_technologies_page(self):
        pass

    def test_can_access_edit_other_page(self):
        pass


class CVEditBasicInformationPageTest(TestCase):

    def test_can_save_basic_information_post_request(self):
        pass

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
