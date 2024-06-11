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

from async_anchio.models.limit_offset_page_employee_schema import LimitOffsetPageEmployeeSchema

class TestLimitOffsetPageEmployeeSchema(unittest.TestCase):
    """LimitOffsetPageEmployeeSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageEmployeeSchema:
        """Test LimitOffsetPageEmployeeSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageEmployeeSchema`
        """
        model = LimitOffsetPageEmployeeSchema()
        if include_optional:
            return LimitOffsetPageEmployeeSchema(
                items = [
                    async_anchio.models.employee_schema.EmployeeSchema(
                        id = '', 
                        created_on = '', 
                        updated_on = '', 
                        first_name = '', 
                        last_name = '', 
                        title = '', 
                        email = '', 
                        company = async_anchio.models.company_schema.CompanySchema(
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
                            last_employee_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_find_employee_app_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            slug = '', ), 
                        employment_status = 'ACTIVE', 
                        employment_type = 'FULL_TIME', 
                        employment_start = '', 
                        employment_end = '', 
                        department_ids = [
                            ''
                            ], )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageEmployeeSchema(
                items = [
                    async_anchio.models.employee_schema.EmployeeSchema(
                        id = '', 
                        created_on = '', 
                        updated_on = '', 
                        first_name = '', 
                        last_name = '', 
                        title = '', 
                        email = '', 
                        company = async_anchio.models.company_schema.CompanySchema(
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
                            last_employee_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_find_employee_app_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            slug = '', ), 
                        employment_status = 'ACTIVE', 
                        employment_type = 'FULL_TIME', 
                        employment_start = '', 
                        employment_end = '', 
                        department_ids = [
                            ''
                            ], )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageEmployeeSchema(self):
        """Test LimitOffsetPageEmployeeSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
