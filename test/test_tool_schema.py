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

from async_anchio.models.tool_schema import ToolSchema

class TestToolSchema(unittest.TestCase):
    """ToolSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ToolSchema:
        """Test ToolSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ToolSchema`
        """
        model = ToolSchema()
        if include_optional:
            return ToolSchema(
                id = '',
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_count = 56,
                name = '',
                description = '',
                logo = '',
                category = async_anchio.models.tool_category_schema.ToolCategorySchema(
                    id = '', 
                    created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    description = '', ),
                country = '',
                has_subprocessor = True,
                hidden_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tags = [
                    ''
                    ]
            )
        else:
            return ToolSchema(
                name = '',
                description = '',
                logo = '',
                country = '',
        )
        """

    def testToolSchema(self):
        """Test ToolSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
