# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from async_anchio.models.o_auth_post_authorization_url import OAuthPostAuthorizationUrl

class TestOAuthPostAuthorizationUrl(unittest.TestCase):
    """OAuthPostAuthorizationUrl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuthPostAuthorizationUrl:
        """Test OAuthPostAuthorizationUrl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuthPostAuthorizationUrl`
        """
        model = OAuthPostAuthorizationUrl()
        if include_optional:
            return OAuthPostAuthorizationUrl(
                authorization_response = '',
                redirect_uri = ''
            )
        else:
            return OAuthPostAuthorizationUrl(
                authorization_response = '',
                redirect_uri = '',
        )
        """

    def testOAuthPostAuthorizationUrl(self):
        """Test OAuthPostAuthorizationUrl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
