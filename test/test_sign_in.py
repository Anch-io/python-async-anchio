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

from async_anchio.models.sign_in import SignIn

class TestSignIn(unittest.TestCase):
    """SignIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignIn:
        """Test SignIn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignIn`
        """
        model = SignIn()
        if include_optional:
            return SignIn(
                code = '',
                redirect_uri = '',
                scope = '',
                grant_type = 'authorization_code'
            )
        else:
            return SignIn(
                code = '',
                redirect_uri = '',
                scope = '',
                grant_type = 'authorization_code',
        )
        """

    def testSignIn(self):
        """Test SignIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
