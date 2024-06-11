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

from async_anchio.models.contract_schema import ContractSchema

class TestContractSchema(unittest.TestCase):
    """ContractSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractSchema:
        """Test ContractSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractSchema`
        """
        model = ContractSchema()
        if include_optional:
            return ContractSchema(
                id = '',
                created_on = '',
                updated_on = '',
                department_ids = [
                    ''
                    ],
                contract_tools = [
                    async_anchio.models.tool_contract_schema.ToolContractSchema(
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
                            ], 
                        seat_limit = 56, 
                        tool_id = '', 
                        contract_id = '', )
                    ],
                name = '',
                start = '',
                end = '',
                signing_date = '',
                contract_amount = 1.337,
                payment_terms = 30,
                payment_frequency = 12,
                justification = '',
                notes = '',
                agreement_link = '',
                renewal_policy = 'AUTO_RENEW',
                contract_signer = async_anchio.models.employee_schema.EmployeeSchema(
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
                        ], ),
                user_count = 56
            )
        else:
            return ContractSchema(
                id = '',
                department_ids = [
                    ''
                    ],
                contract_tools = [
                    async_anchio.models.tool_contract_schema.ToolContractSchema(
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
                            ], 
                        seat_limit = 56, 
                        tool_id = '', 
                        contract_id = '', )
                    ],
                start = '',
                payment_terms = 30,
                payment_frequency = 12,
                justification = '',
                renewal_policy = 'AUTO_RENEW',
        )
        """

    def testContractSchema(self):
        """Test ContractSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
