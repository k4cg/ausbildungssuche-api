"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 1c852184-1944-4a9e-a093-5cc078981294  **ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.ausbildungssuche.api.default_api import DefaultApi  # noqa: E501

from deutschland import ausbildungssuche


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ausbildungsdetails(self):
        """Test case for ausbildungsdetails

        Ausbildungsdetails  # noqa: E501
        """
        pass

    def test_ausbildungssuche(self):
        """Test case for ausbildungssuche

        Ausbildungssuche  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
