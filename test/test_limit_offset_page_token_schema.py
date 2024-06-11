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

from async_anchio.models.limit_offset_page_token_schema import LimitOffsetPageTokenSchema

class TestLimitOffsetPageTokenSchema(unittest.TestCase):
    """LimitOffsetPageTokenSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageTokenSchema:
        """Test LimitOffsetPageTokenSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageTokenSchema`
        """
        model = LimitOffsetPageTokenSchema()
        if include_optional:
            return LimitOffsetPageTokenSchema(
                items = [
                    async_anchio.models.token_schema.TokenSchema(
                        id = '', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = '', 
                        token_type = null, 
                        expires_in = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date_invalidated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        provider = 'google', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageTokenSchema(
                items = [
                    async_anchio.models.token_schema.TokenSchema(
                        id = '', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = '', 
                        token_type = null, 
                        expires_in = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date_invalidated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        provider = 'google', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageTokenSchema(self):
        """Test LimitOffsetPageTokenSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
