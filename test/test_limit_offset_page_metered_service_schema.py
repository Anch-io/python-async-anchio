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

from async_anchio.models.limit_offset_page_metered_service_schema import LimitOffsetPageMeteredServiceSchema

class TestLimitOffsetPageMeteredServiceSchema(unittest.TestCase):
    """LimitOffsetPageMeteredServiceSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageMeteredServiceSchema:
        """Test LimitOffsetPageMeteredServiceSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageMeteredServiceSchema`
        """
        model = LimitOffsetPageMeteredServiceSchema()
        if include_optional:
            return LimitOffsetPageMeteredServiceSchema(
                items = [
                    async_anchio.models.metered_service_schema.MeteredServiceSchema(
                        created_on = '', 
                        updated_on = '', 
                        id = '', 
                        name = '', 
                        description = '', 
                        tool_contract = '', 
                        source = 'lang_smith', 
                        seven_day_usage = 56, 
                        thirty_day_usage = 56, 
                        ninety_day_usage = 56, )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageMeteredServiceSchema(
                items = [
                    async_anchio.models.metered_service_schema.MeteredServiceSchema(
                        created_on = '', 
                        updated_on = '', 
                        id = '', 
                        name = '', 
                        description = '', 
                        tool_contract = '', 
                        source = 'lang_smith', 
                        seven_day_usage = 56, 
                        thirty_day_usage = 56, 
                        ninety_day_usage = 56, )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageMeteredServiceSchema(self):
        """Test LimitOffsetPageMeteredServiceSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
