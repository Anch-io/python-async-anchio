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

from async_anchio.models.plaid_link_token_schema import PlaidLinkTokenSchema

class TestPlaidLinkTokenSchema(unittest.TestCase):
    """PlaidLinkTokenSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaidLinkTokenSchema:
        """Test PlaidLinkTokenSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaidLinkTokenSchema`
        """
        model = PlaidLinkTokenSchema()
        if include_optional:
            return PlaidLinkTokenSchema(
                link_token = ''
            )
        else:
            return PlaidLinkTokenSchema(
                link_token = '',
        )
        """

    def testPlaidLinkTokenSchema(self):
        """Test PlaidLinkTokenSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
