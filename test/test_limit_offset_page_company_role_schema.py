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

from async_anchio.models.limit_offset_page_company_role_schema import LimitOffsetPageCompanyRoleSchema

class TestLimitOffsetPageCompanyRoleSchema(unittest.TestCase):
    """LimitOffsetPageCompanyRoleSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageCompanyRoleSchema:
        """Test LimitOffsetPageCompanyRoleSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageCompanyRoleSchema`
        """
        model = LimitOffsetPageCompanyRoleSchema()
        if include_optional:
            return LimitOffsetPageCompanyRoleSchema(
                items = [
                    async_anchio.models.company_role_schema.CompanyRoleSchema(
                        id = '', 
                        name = '', 
                        description = '', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageCompanyRoleSchema(
                items = [
                    async_anchio.models.company_role_schema.CompanyRoleSchema(
                        id = '', 
                        name = '', 
                        description = '', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageCompanyRoleSchema(self):
        """Test LimitOffsetPageCompanyRoleSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
