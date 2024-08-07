# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.9
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from async_anchio.models.company_schema_input import CompanySchemaInput

class TestCompanySchemaInput(unittest.TestCase):
    """CompanySchemaInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanySchemaInput:
        """Test CompanySchemaInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanySchemaInput`
        """
        model = CompanySchemaInput()
        if include_optional:
            return CompanySchemaInput(
                id = '',
                allowed_origins = [
                    ''
                    ],
                has_customer = True,
                is_trial_active = True,
                is_subscription_active = True,
                employee_count = 56,
                name = '',
                handle = '',
                keycloak_group = '',
                description = '',
                logo = '',
                email = '',
                phone = '',
                category = '',
                address_1 = '',
                address_2 = '',
                city = '',
                state = '',
                country = '',
                postal_code = '',
                slug = '',
                sync_status = async_anchio.models.company_sync_status.CompanySyncStatus(
                    employee_sync = null, 
                    find_employee_app_sync = null, 
                    activity_sync = null, 
                    plaid_sync = null, 
                    lang_smith_sync = null, ),
                allow_public_company_access_page = True
            )
        else:
            return CompanySchemaInput(
                name = '',
                handle = '',
                country = '',
                sync_status = async_anchio.models.company_sync_status.CompanySyncStatus(
                    employee_sync = null, 
                    find_employee_app_sync = null, 
                    activity_sync = null, 
                    plaid_sync = null, 
                    lang_smith_sync = null, ),
        )
        """

    def testCompanySchemaInput(self):
        """Test CompanySchemaInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
