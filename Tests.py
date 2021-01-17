import pytest
from Accounting import Accounting
from AccountingBase import directories, documents
from yandex import Yandex
import requests

yandex_token = ''


class TestAccounting:

    def setup(self):
        self.accounting_1 = Accounting(documents, directories)

    def teardown(self):
        pass

    def test_add_new_doc(self):
        # user = Accounting(documents, directories)
        assert self.accounting_1.add_new_doc('45', 'passport', 'midfinup1', '5')

    def test_delete_doc(self):
        assert self.accounting_1.delete_doc('45')

    def test_get_doc_list(self):
        assert self.accounting_1.get_doc_shelf('11-2')


class TestYandexDisc:

    def setup(self):
        self.token = yandex_token
        self.yandex_disc1 = Yandex(self.token)

    def teardown(self):
        pass

    def test_create_folder(self):
        response = self.yandex_disc1.create_folder('vsaf')
        assert response.status_code == 201


class TestYandexDiscFails:

    def setup(self):
        self.token = yandex_token
        self.yandex_disc2 = Yandex(self.token)
        self.folder = 'test_folder'
        self.HEADERS = {"Authorization": f"OAuth {self.token}"}

    def teardown(self):
        pass

    def test_fail_create_folder_409(self):
        response = self.yandex_disc2.create_folder(self.folder)
        assert response.status_code == 409

    def test_fail_create_folder_400(self):
        self.folder = 90
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=self.HEADERS)
        assert response.status_code == 400

    def test_fail_create_folder_401(self):
        data = {'path': self.folder}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=data)
        assert response.status_code == 401

    def test_fail_create_folder_404(self):
        data = {'path': self.folder}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resorces', headers=self.HEADERS, params=data)
        assert response.status_code == 404
