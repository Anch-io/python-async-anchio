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

from async_anchio.models.limit_offset_page_employee_role_tool_schema import LimitOffsetPageEmployeeRoleToolSchema

class TestLimitOffsetPageEmployeeRoleToolSchema(unittest.TestCase):
    """LimitOffsetPageEmployeeRoleToolSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageEmployeeRoleToolSchema:
        """Test LimitOffsetPageEmployeeRoleToolSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageEmployeeRoleToolSchema`
        """
        model = LimitOffsetPageEmployeeRoleToolSchema()
        if include_optional:
            return LimitOffsetPageEmployeeRoleToolSchema(
                items = [
                    async_anchio.models.employee_role_tool_schema.EmployeeRoleToolSchema(
                        created_on = '', 
                        updated_on = '', 
                        id = '', 
                        employee_role = '', 
                        tool = '', 
                        accesses = [
                            ''
                            ], 
                        notes = '', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageEmployeeRoleToolSchema(
                items = [
                    async_anchio.models.employee_role_tool_schema.EmployeeRoleToolSchema(
                        created_on = '', 
                        updated_on = '', 
                        id = '', 
                        employee_role = '', 
                        tool = '', 
                        accesses = [
                            ''
                            ], 
                        notes = '', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageEmployeeRoleToolSchema(self):
        """Test LimitOffsetPageEmployeeRoleToolSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()