# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.9
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ScopeEnum(str, Enum):
    """
    ScopeEnum
    """

    """
    allowed enum values
    """
    ADMIN = 'admin'
    ADMIN_DOT_LOGENTRY = 'admin.logentry'
    ADMIN_DOT_LOGENTRY_DOT_CREATE = 'admin.logentry.create'
    ADMIN_DOT_LOGENTRY_DOT_DELETE = 'admin.logentry.delete'
    ADMIN_DOT_LOGENTRY_DOT_READ = 'admin.logentry.read'
    ADMIN_DOT_LOGENTRY_DOT_UPDATE = 'admin.logentry.update'
    ANCH_AUTH = 'anch_auth'
    ANCH_AUTH_DOT_APIKEY = 'anch_auth.apikey'
    ANCH_AUTH_DOT_APIKEY_DOT_CREATE = 'anch_auth.apikey.create'
    ANCH_AUTH_DOT_APIKEY_DOT_DELETE = 'anch_auth.apikey.delete'
    ANCH_AUTH_DOT_APIKEY_DOT_READ = 'anch_auth.apikey.read'
    ANCH_AUTH_DOT_APIKEY_DOT_UPDATE = 'anch_auth.apikey.update'
    ANCH_AUTH_DOT_COMPANY = 'anch_auth.company'
    ANCH_AUTH_DOT_COMPANY_DOT_CREATE = 'anch_auth.company.create'
    ANCH_AUTH_DOT_COMPANY_DOT_DELETE = 'anch_auth.company.delete'
    ANCH_AUTH_DOT_COMPANY_DOT_READ = 'anch_auth.company.read'
    ANCH_AUTH_DOT_COMPANY_DOT_UPDATE = 'anch_auth.company.update'
    ANCH_AUTH_DOT_COMPANYCATEGORY = 'anch_auth.companycategory'
    ANCH_AUTH_DOT_COMPANYCATEGORY_DOT_CREATE = 'anch_auth.companycategory.create'
    ANCH_AUTH_DOT_COMPANYCATEGORY_DOT_DELETE = 'anch_auth.companycategory.delete'
    ANCH_AUTH_DOT_COMPANYCATEGORY_DOT_READ = 'anch_auth.companycategory.read'
    ANCH_AUTH_DOT_COMPANYCATEGORY_DOT_UPDATE = 'anch_auth.companycategory.update'
    ANCH_AUTH_DOT_COMPANYPERMISSION = 'anch_auth.companypermission'
    ANCH_AUTH_DOT_COMPANYPERMISSION_DOT_CREATE = 'anch_auth.companypermission.create'
    ANCH_AUTH_DOT_COMPANYPERMISSION_DOT_DELETE = 'anch_auth.companypermission.delete'
    ANCH_AUTH_DOT_COMPANYPERMISSION_DOT_READ = 'anch_auth.companypermission.read'
    ANCH_AUTH_DOT_COMPANYPERMISSION_DOT_UPDATE = 'anch_auth.companypermission.update'
    ANCH_AUTH_DOT_COMPANYPERMISSIONGROUP = 'anch_auth.companypermissiongroup'
    ANCH_AUTH_DOT_COMPANYPERMISSIONGROUP_DOT_CREATE = 'anch_auth.companypermissiongroup.create'
    ANCH_AUTH_DOT_COMPANYPERMISSIONGROUP_DOT_DELETE = 'anch_auth.companypermissiongroup.delete'
    ANCH_AUTH_DOT_COMPANYPERMISSIONGROUP_DOT_READ = 'anch_auth.companypermissiongroup.read'
    ANCH_AUTH_DOT_COMPANYPERMISSIONGROUP_DOT_UPDATE = 'anch_auth.companypermissiongroup.update'
    ANCH_AUTH_DOT_COMPANYROLE = 'anch_auth.companyrole'
    ANCH_AUTH_DOT_COMPANYROLE_DOT_CREATE = 'anch_auth.companyrole.create'
    ANCH_AUTH_DOT_COMPANYROLE_DOT_DELETE = 'anch_auth.companyrole.delete'
    ANCH_AUTH_DOT_COMPANYROLE_DOT_READ = 'anch_auth.companyrole.read'
    ANCH_AUTH_DOT_COMPANYROLE_DOT_UPDATE = 'anch_auth.companyrole.update'
    ANCH_AUTH_DOT_COMPANYROLEPERMISSION = 'anch_auth.companyrolepermission'
    ANCH_AUTH_DOT_COMPANYROLEPERMISSION_DOT_CREATE = 'anch_auth.companyrolepermission.create'
    ANCH_AUTH_DOT_COMPANYROLEPERMISSION_DOT_DELETE = 'anch_auth.companyrolepermission.delete'
    ANCH_AUTH_DOT_COMPANYROLEPERMISSION_DOT_READ = 'anch_auth.companyrolepermission.read'
    ANCH_AUTH_DOT_COMPANYROLEPERMISSION_DOT_UPDATE = 'anch_auth.companyrolepermission.update'
    ANCH_AUTH_DOT_KEY = 'anch_auth.key'
    ANCH_AUTH_DOT_KEY_DOT_CREATE = 'anch_auth.key.create'
    ANCH_AUTH_DOT_KEY_DOT_DELETE = 'anch_auth.key.delete'
    ANCH_AUTH_DOT_KEY_DOT_READ = 'anch_auth.key.read'
    ANCH_AUTH_DOT_KEY_DOT_UPDATE = 'anch_auth.key.update'
    ANCH_AUTH_DOT_OAUTH2EVENT = 'anch_auth.oauth2event'
    ANCH_AUTH_DOT_OAUTH2EVENT_DOT_CREATE = 'anch_auth.oauth2event.create'
    ANCH_AUTH_DOT_OAUTH2EVENT_DOT_DELETE = 'anch_auth.oauth2event.delete'
    ANCH_AUTH_DOT_OAUTH2EVENT_DOT_READ = 'anch_auth.oauth2event.read'
    ANCH_AUTH_DOT_OAUTH2EVENT_DOT_UPDATE = 'anch_auth.oauth2event.update'
    ANCH_AUTH_DOT_OAUTHTOKEN = 'anch_auth.oauthtoken'
    ANCH_AUTH_DOT_OAUTHTOKEN_DOT_CREATE = 'anch_auth.oauthtoken.create'
    ANCH_AUTH_DOT_OAUTHTOKEN_DOT_DELETE = 'anch_auth.oauthtoken.delete'
    ANCH_AUTH_DOT_OAUTHTOKEN_DOT_READ = 'anch_auth.oauthtoken.read'
    ANCH_AUTH_DOT_OAUTHTOKEN_DOT_UPDATE = 'anch_auth.oauthtoken.update'
    ANCH_AUTH_DOT_USERLICENSE = 'anch_auth.userlicense'
    ANCH_AUTH_DOT_USERLICENSE_DOT_CREATE = 'anch_auth.userlicense.create'
    ANCH_AUTH_DOT_USERLICENSE_DOT_DELETE = 'anch_auth.userlicense.delete'
    ANCH_AUTH_DOT_USERLICENSE_DOT_READ = 'anch_auth.userlicense.read'
    ANCH_AUTH_DOT_USERLICENSE_DOT_UPDATE = 'anch_auth.userlicense.update'
    ANCH_CORP = 'anch_corp'
    ANCH_CORP_DOT_BANKACCOUNT = 'anch_corp.bankaccount'
    ANCH_CORP_DOT_BANKACCOUNT_DOT_CREATE = 'anch_corp.bankaccount.create'
    ANCH_CORP_DOT_BANKACCOUNT_DOT_DELETE = 'anch_corp.bankaccount.delete'
    ANCH_CORP_DOT_BANKACCOUNT_DOT_READ = 'anch_corp.bankaccount.read'
    ANCH_CORP_DOT_BANKACCOUNT_DOT_UPDATE = 'anch_corp.bankaccount.update'
    ANCH_CORP_DOT_CONTRACT = 'anch_corp.contract'
    ANCH_CORP_DOT_CONTRACT_DOT_CREATE = 'anch_corp.contract.create'
    ANCH_CORP_DOT_CONTRACT_DOT_DELETE = 'anch_corp.contract.delete'
    ANCH_CORP_DOT_CONTRACT_DOT_READ = 'anch_corp.contract.read'
    ANCH_CORP_DOT_CONTRACT_DOT_UPDATE = 'anch_corp.contract.update'
    ANCH_CORP_DOT_CONTRACTTOOL = 'anch_corp.contracttool'
    ANCH_CORP_DOT_CONTRACTTOOL_DOT_CREATE = 'anch_corp.contracttool.create'
    ANCH_CORP_DOT_CONTRACTTOOL_DOT_DELETE = 'anch_corp.contracttool.delete'
    ANCH_CORP_DOT_CONTRACTTOOL_DOT_READ = 'anch_corp.contracttool.read'
    ANCH_CORP_DOT_CONTRACTTOOL_DOT_UPDATE = 'anch_corp.contracttool.update'
    ANCH_CORP_DOT_CONTRACTTOOLTRANSACTION = 'anch_corp.contracttooltransaction'
    ANCH_CORP_DOT_CONTRACTTOOLTRANSACTION_DOT_CREATE = 'anch_corp.contracttooltransaction.create'
    ANCH_CORP_DOT_CONTRACTTOOLTRANSACTION_DOT_DELETE = 'anch_corp.contracttooltransaction.delete'
    ANCH_CORP_DOT_CONTRACTTOOLTRANSACTION_DOT_READ = 'anch_corp.contracttooltransaction.read'
    ANCH_CORP_DOT_CONTRACTTOOLTRANSACTION_DOT_UPDATE = 'anch_corp.contracttooltransaction.update'
    ANCH_CORP_DOT_CONTRACTTRANSACTION = 'anch_corp.contracttransaction'
    ANCH_CORP_DOT_CONTRACTTRANSACTION_DOT_CREATE = 'anch_corp.contracttransaction.create'
    ANCH_CORP_DOT_CONTRACTTRANSACTION_DOT_DELETE = 'anch_corp.contracttransaction.delete'
    ANCH_CORP_DOT_CONTRACTTRANSACTION_DOT_READ = 'anch_corp.contracttransaction.read'
    ANCH_CORP_DOT_CONTRACTTRANSACTION_DOT_UPDATE = 'anch_corp.contracttransaction.update'
    ANCH_CORP_DOT_DEPARTMENT = 'anch_corp.department'
    ANCH_CORP_DOT_DEPARTMENT_DOT_CREATE = 'anch_corp.department.create'
    ANCH_CORP_DOT_DEPARTMENT_DOT_DELETE = 'anch_corp.department.delete'
    ANCH_CORP_DOT_DEPARTMENT_DOT_READ = 'anch_corp.department.read'
    ANCH_CORP_DOT_DEPARTMENT_DOT_UPDATE = 'anch_corp.department.update'
    ANCH_CORP_DOT_DEPARTMENTCONTRACT = 'anch_corp.departmentcontract'
    ANCH_CORP_DOT_DEPARTMENTCONTRACT_DOT_CREATE = 'anch_corp.departmentcontract.create'
    ANCH_CORP_DOT_DEPARTMENTCONTRACT_DOT_DELETE = 'anch_corp.departmentcontract.delete'
    ANCH_CORP_DOT_DEPARTMENTCONTRACT_DOT_READ = 'anch_corp.departmentcontract.read'
    ANCH_CORP_DOT_DEPARTMENTCONTRACT_DOT_UPDATE = 'anch_corp.departmentcontract.update'
    ANCH_CORP_DOT_DEPARTMENTMEMBERSHIP = 'anch_corp.departmentmembership'
    ANCH_CORP_DOT_DEPARTMENTMEMBERSHIP_DOT_CREATE = 'anch_corp.departmentmembership.create'
    ANCH_CORP_DOT_DEPARTMENTMEMBERSHIP_DOT_DELETE = 'anch_corp.departmentmembership.delete'
    ANCH_CORP_DOT_DEPARTMENTMEMBERSHIP_DOT_READ = 'anch_corp.departmentmembership.read'
    ANCH_CORP_DOT_DEPARTMENTMEMBERSHIP_DOT_UPDATE = 'anch_corp.departmentmembership.update'
    ANCH_CORP_DOT_EMPLOYEE = 'anch_corp.employee'
    ANCH_CORP_DOT_EMPLOYEE_DOT_CREATE = 'anch_corp.employee.create'
    ANCH_CORP_DOT_EMPLOYEE_DOT_DELETE = 'anch_corp.employee.delete'
    ANCH_CORP_DOT_EMPLOYEE_DOT_READ = 'anch_corp.employee.read'
    ANCH_CORP_DOT_EMPLOYEE_DOT_UPDATE = 'anch_corp.employee.update'
    ANCH_CORP_DOT_EMPLOYEEROLE = 'anch_corp.employeerole'
    ANCH_CORP_DOT_EMPLOYEEROLE_DOT_CREATE = 'anch_corp.employeerole.create'
    ANCH_CORP_DOT_EMPLOYEEROLE_DOT_DELETE = 'anch_corp.employeerole.delete'
    ANCH_CORP_DOT_EMPLOYEEROLE_DOT_READ = 'anch_corp.employeerole.read'
    ANCH_CORP_DOT_EMPLOYEEROLE_DOT_UPDATE = 'anch_corp.employeerole.update'
    ANCH_CORP_DOT_EMPLOYEEROLETOOL = 'anch_corp.employeeroletool'
    ANCH_CORP_DOT_EMPLOYEEROLETOOL_DOT_CREATE = 'anch_corp.employeeroletool.create'
    ANCH_CORP_DOT_EMPLOYEEROLETOOL_DOT_DELETE = 'anch_corp.employeeroletool.delete'
    ANCH_CORP_DOT_EMPLOYEEROLETOOL_DOT_READ = 'anch_corp.employeeroletool.read'
    ANCH_CORP_DOT_EMPLOYEEROLETOOL_DOT_UPDATE = 'anch_corp.employeeroletool.update'
    ANCH_CORP_DOT_TRANSACTION = 'anch_corp.transaction'
    ANCH_CORP_DOT_TRANSACTION_DOT_CREATE = 'anch_corp.transaction.create'
    ANCH_CORP_DOT_TRANSACTION_DOT_DELETE = 'anch_corp.transaction.delete'
    ANCH_CORP_DOT_TRANSACTION_DOT_READ = 'anch_corp.transaction.read'
    ANCH_CORP_DOT_TRANSACTION_DOT_UPDATE = 'anch_corp.transaction.update'
    ANCH_METERING = 'anch_metering'
    ANCH_METERING_DOT_METEREDALERT = 'anch_metering.meteredalert'
    ANCH_METERING_DOT_METEREDALERT_DOT_CREATE = 'anch_metering.meteredalert.create'
    ANCH_METERING_DOT_METEREDALERT_DOT_DELETE = 'anch_metering.meteredalert.delete'
    ANCH_METERING_DOT_METEREDALERT_DOT_READ = 'anch_metering.meteredalert.read'
    ANCH_METERING_DOT_METEREDALERT_DOT_UPDATE = 'anch_metering.meteredalert.update'
    ANCH_METERING_DOT_METEREDSERVICE = 'anch_metering.meteredservice'
    ANCH_METERING_DOT_METEREDSERVICE_DOT_CREATE = 'anch_metering.meteredservice.create'
    ANCH_METERING_DOT_METEREDSERVICE_DOT_DELETE = 'anch_metering.meteredservice.delete'
    ANCH_METERING_DOT_METEREDSERVICE_DOT_READ = 'anch_metering.meteredservice.read'
    ANCH_METERING_DOT_METEREDSERVICE_DOT_UPDATE = 'anch_metering.meteredservice.update'
    ANCH_METERING_DOT_METEREDSERVICEMETRIC = 'anch_metering.meteredservicemetric'
    ANCH_METERING_DOT_METEREDSERVICEMETRIC_DOT_CREATE = 'anch_metering.meteredservicemetric.create'
    ANCH_METERING_DOT_METEREDSERVICEMETRIC_DOT_DELETE = 'anch_metering.meteredservicemetric.delete'
    ANCH_METERING_DOT_METEREDSERVICEMETRIC_DOT_READ = 'anch_metering.meteredservicemetric.read'
    ANCH_METERING_DOT_METEREDSERVICEMETRIC_DOT_UPDATE = 'anch_metering.meteredservicemetric.update'
    ANCH_METERING_DOT_METERENTRY = 'anch_metering.meterentry'
    ANCH_METERING_DOT_METERENTRY_DOT_CREATE = 'anch_metering.meterentry.create'
    ANCH_METERING_DOT_METERENTRY_DOT_DELETE = 'anch_metering.meterentry.delete'
    ANCH_METERING_DOT_METERENTRY_DOT_READ = 'anch_metering.meterentry.read'
    ANCH_METERING_DOT_METERENTRY_DOT_UPDATE = 'anch_metering.meterentry.update'
    ANCH_METERING_DOT_METERENTRYGROUP = 'anch_metering.meterentrygroup'
    ANCH_METERING_DOT_METERENTRYGROUP_DOT_CREATE = 'anch_metering.meterentrygroup.create'
    ANCH_METERING_DOT_METERENTRYGROUP_DOT_DELETE = 'anch_metering.meterentrygroup.delete'
    ANCH_METERING_DOT_METERENTRYGROUP_DOT_READ = 'anch_metering.meterentrygroup.read'
    ANCH_METERING_DOT_METERENTRYGROUP_DOT_UPDATE = 'anch_metering.meterentrygroup.update'
    ANCH_NOTIFICATION = 'anch_notification'
    ANCH_NOTIFICATION_DOT_NOTIFICATION = 'anch_notification.notification'
    ANCH_NOTIFICATION_DOT_NOTIFICATION_DOT_CREATE = 'anch_notification.notification.create'
    ANCH_NOTIFICATION_DOT_NOTIFICATION_DOT_DELETE = 'anch_notification.notification.delete'
    ANCH_NOTIFICATION_DOT_NOTIFICATION_DOT_READ = 'anch_notification.notification.read'
    ANCH_NOTIFICATION_DOT_NOTIFICATION_DOT_UPDATE = 'anch_notification.notification.update'
    ANCH_NOTIFICATION_DOT_NOTIFICATIONCHANNEL = 'anch_notification.notificationchannel'
    ANCH_NOTIFICATION_DOT_NOTIFICATIONCHANNEL_DOT_CREATE = 'anch_notification.notificationchannel.create'
    ANCH_NOTIFICATION_DOT_NOTIFICATIONCHANNEL_DOT_DELETE = 'anch_notification.notificationchannel.delete'
    ANCH_NOTIFICATION_DOT_NOTIFICATIONCHANNEL_DOT_READ = 'anch_notification.notificationchannel.read'
    ANCH_NOTIFICATION_DOT_NOTIFICATIONCHANNEL_DOT_UPDATE = 'anch_notification.notificationchannel.update'
    ANCH_TOOLS = 'anch_tools'
    ANCH_TOOLS_DOT_TAGTHOUGH = 'anch_tools.tagthough'
    ANCH_TOOLS_DOT_TAGTHOUGH_DOT_CREATE = 'anch_tools.tagthough.create'
    ANCH_TOOLS_DOT_TAGTHOUGH_DOT_DELETE = 'anch_tools.tagthough.delete'
    ANCH_TOOLS_DOT_TAGTHOUGH_DOT_READ = 'anch_tools.tagthough.read'
    ANCH_TOOLS_DOT_TAGTHOUGH_DOT_UPDATE = 'anch_tools.tagthough.update'
    ANCH_TOOLS_DOT_TOOL = 'anch_tools.tool'
    ANCH_TOOLS_DOT_TOOL_DOT_CREATE = 'anch_tools.tool.create'
    ANCH_TOOLS_DOT_TOOL_DOT_DELETE = 'anch_tools.tool.delete'
    ANCH_TOOLS_DOT_TOOL_DOT_READ = 'anch_tools.tool.read'
    ANCH_TOOLS_DOT_TOOL_DOT_UPDATE = 'anch_tools.tool.update'
    ANCH_TOOLS_DOT_TOOLACCESS = 'anch_tools.toolaccess'
    ANCH_TOOLS_DOT_TOOLACCESS_DOT_CREATE = 'anch_tools.toolaccess.create'
    ANCH_TOOLS_DOT_TOOLACCESS_DOT_DELETE = 'anch_tools.toolaccess.delete'
    ANCH_TOOLS_DOT_TOOLACCESS_DOT_READ = 'anch_tools.toolaccess.read'
    ANCH_TOOLS_DOT_TOOLACCESS_DOT_UPDATE = 'anch_tools.toolaccess.update'
    ANCH_TOOLS_DOT_TOOLCATEGORY = 'anch_tools.toolcategory'
    ANCH_TOOLS_DOT_TOOLCATEGORY_DOT_CREATE = 'anch_tools.toolcategory.create'
    ANCH_TOOLS_DOT_TOOLCATEGORY_DOT_DELETE = 'anch_tools.toolcategory.delete'
    ANCH_TOOLS_DOT_TOOLCATEGORY_DOT_READ = 'anch_tools.toolcategory.read'
    ANCH_TOOLS_DOT_TOOLCATEGORY_DOT_UPDATE = 'anch_tools.toolcategory.update'
    ANCH_TOOLS_DOT_TOOLUSERACCESS = 'anch_tools.tooluseraccess'
    ANCH_TOOLS_DOT_TOOLUSERACCESS_DOT_CREATE = 'anch_tools.tooluseraccess.create'
    ANCH_TOOLS_DOT_TOOLUSERACCESS_DOT_DELETE = 'anch_tools.tooluseraccess.delete'
    ANCH_TOOLS_DOT_TOOLUSERACCESS_DOT_READ = 'anch_tools.tooluseraccess.read'
    ANCH_TOOLS_DOT_TOOLUSERACCESS_DOT_UPDATE = 'anch_tools.tooluseraccess.update'
    EMAIL = 'email'
    PROFILE = 'profile'
    OPENAPI = 'openapi'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScopeEnum from a JSON string"""
        return cls(json.loads(json_str))


