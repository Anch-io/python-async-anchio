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

from async_anchio.models.update_employee_schema import UpdateEmployeeSchema

class TestUpdateEmployeeSchema(unittest.TestCase):
    """UpdateEmployeeSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateEmployeeSchema:
        """Test UpdateEmployeeSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateEmployeeSchema`
        """
        model = UpdateEmployeeSchema()
        if include_optional:
            return UpdateEmployeeSchema(
                id = '',
                first_name = '',
                last_name = '',
                email = '',
                employment_status = 'ACTIVE',
                employment_type = 'FULL_TIME',
                department_ids = [
                    ''
                    ],
                employment_start = '',
                employment_end = '',
                title = ''
            )
        else:
            return UpdateEmployeeSchema(
                id = '',
                first_name = '',
                last_name = '',
                email = '',
                employment_status = 'ACTIVE',
                employment_type = 'FULL_TIME',
                employment_start = '',
                title = '',
        )
        """

    def testUpdateEmployeeSchema(self):
        """Test UpdateEmployeeSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
