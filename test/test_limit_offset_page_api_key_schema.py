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

from async_anchio.models.limit_offset_page_api_key_schema import LimitOffsetPageAPIKeySchema

class TestLimitOffsetPageAPIKeySchema(unittest.TestCase):
    """LimitOffsetPageAPIKeySchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageAPIKeySchema:
        """Test LimitOffsetPageAPIKeySchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageAPIKeySchema`
        """
        model = LimitOffsetPageAPIKeySchema()
        if include_optional:
            return LimitOffsetPageAPIKeySchema(
                items = [
                    async_anchio.models.api_key_schema.APIKeySchema(
                        id = '', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        key = '', 
                        enabled = True, 
                        provider = 'BREX', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageAPIKeySchema(
                items = [
                    async_anchio.models.api_key_schema.APIKeySchema(
                        id = '', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        key = '', 
                        enabled = True, 
                        provider = 'BREX', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageAPIKeySchema(self):
        """Test LimitOffsetPageAPIKeySchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
