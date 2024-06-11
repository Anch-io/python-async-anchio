# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.3
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


class PermissionEnum(str, Enum):
    """
    PermissionEnum
    """

    """
    allowed enum values
    """
    ACTIONLOG_DOT_CREATE = 'actionlog.create'
    ACTIONLOG_DOT_DELETE = 'actionlog.delete'
    ACTIONLOG_DOT_READ = 'actionlog.read'
    ACTIONLOG_DOT_UPDATE = 'actionlog.update'
    APIKEY_DOT_CREATE = 'apikey.create'
    APIKEY_DOT_DELETE = 'apikey.delete'
    APIKEY_DOT_READ = 'apikey.read'
    APIKEY_DOT_UPDATE = 'apikey.update'
    BANKACCOUNT_DOT_CREATE = 'bankaccount.create'
    BANKACCOUNT_DOT_DELETE = 'bankaccount.delete'
    BANKACCOUNT_DOT_READ = 'bankaccount.read'
    BANKACCOUNT_DOT_UPDATE = 'bankaccount.update'
    CHORDCOUNTER_DOT_CREATE = 'chordcounter.create'
    CHORDCOUNTER_DOT_DELETE = 'chordcounter.delete'
    CHORDCOUNTER_DOT_READ = 'chordcounter.read'
    CHORDCOUNTER_DOT_UPDATE = 'chordcounter.update'
    COMPANY_DOT_CREATE = 'company.create'
    COMPANY_DOT_DELETE = 'company.delete'
    COMPANY_DOT_READ = 'company.read'
    COMPANY_DOT_UPDATE = 'company.update'
    COMPANYCATEGORY_DOT_CREATE = 'companycategory.create'
    COMPANYCATEGORY_DOT_DELETE = 'companycategory.delete'
    COMPANYCATEGORY_DOT_READ = 'companycategory.read'
    COMPANYCATEGORY_DOT_UPDATE = 'companycategory.update'
    COMPANYPERMISSION_DOT_CREATE = 'companypermission.create'
    COMPANYPERMISSION_DOT_DELETE = 'companypermission.delete'
    COMPANYPERMISSION_DOT_READ = 'companypermission.read'
    COMPANYPERMISSION_DOT_UPDATE = 'companypermission.update'
    COMPANYPERMISSIONGROUP_DOT_CREATE = 'companypermissiongroup.create'
    COMPANYPERMISSIONGROUP_DOT_DELETE = 'companypermissiongroup.delete'
    COMPANYPERMISSIONGROUP_DOT_READ = 'companypermissiongroup.read'
    COMPANYPERMISSIONGROUP_DOT_UPDATE = 'companypermissiongroup.update'
    COMPANYROLE_DOT_CREATE = 'companyrole.create'
    COMPANYROLE_DOT_DELETE = 'companyrole.delete'
    COMPANYROLE_DOT_READ = 'companyrole.read'
    COMPANYROLE_DOT_UPDATE = 'companyrole.update'
    COMPANYROLEPERMISSION_DOT_CREATE = 'companyrolepermission.create'
    COMPANYROLEPERMISSION_DOT_DELETE = 'companyrolepermission.delete'
    COMPANYROLEPERMISSION_DOT_READ = 'companyrolepermission.read'
    COMPANYROLEPERMISSION_DOT_UPDATE = 'companyrolepermission.update'
    CONTENTTYPE_DOT_CREATE = 'contenttype.create'
    CONTENTTYPE_DOT_DELETE = 'contenttype.delete'
    CONTENTTYPE_DOT_READ = 'contenttype.read'
    CONTENTTYPE_DOT_UPDATE = 'contenttype.update'
    CONTRACT_DOT_CREATE = 'contract.create'
    CONTRACT_DOT_DELETE = 'contract.delete'
    CONTRACT_DOT_READ = 'contract.read'
    CONTRACT_DOT_UPDATE = 'contract.update'
    CONTRACTTOOL_DOT_CREATE = 'contracttool.create'
    CONTRACTTOOL_DOT_DELETE = 'contracttool.delete'
    CONTRACTTOOL_DOT_READ = 'contracttool.read'
    CONTRACTTOOL_DOT_UPDATE = 'contracttool.update'
    CONTRACTTOOLTRANSACTION_DOT_CREATE = 'contracttooltransaction.create'
    CONTRACTTOOLTRANSACTION_DOT_DELETE = 'contracttooltransaction.delete'
    CONTRACTTOOLTRANSACTION_DOT_READ = 'contracttooltransaction.read'
    CONTRACTTOOLTRANSACTION_DOT_UPDATE = 'contracttooltransaction.update'
    CONTRACTTRANSACTION_DOT_CREATE = 'contracttransaction.create'
    CONTRACTTRANSACTION_DOT_DELETE = 'contracttransaction.delete'
    CONTRACTTRANSACTION_DOT_READ = 'contracttransaction.read'
    CONTRACTTRANSACTION_DOT_UPDATE = 'contracttransaction.update'
    DEPARTMENT_DOT_CREATE = 'department.create'
    DEPARTMENT_DOT_DELETE = 'department.delete'
    DEPARTMENT_DOT_READ = 'department.read'
    DEPARTMENT_DOT_UPDATE = 'department.update'
    DEPARTMENTCONTRACT_DOT_CREATE = 'departmentcontract.create'
    DEPARTMENTCONTRACT_DOT_DELETE = 'departmentcontract.delete'
    DEPARTMENTCONTRACT_DOT_READ = 'departmentcontract.read'
    DEPARTMENTCONTRACT_DOT_UPDATE = 'departmentcontract.update'
    DEPARTMENTMEMBERSHIP_DOT_CREATE = 'departmentmembership.create'
    DEPARTMENTMEMBERSHIP_DOT_DELETE = 'departmentmembership.delete'
    DEPARTMENTMEMBERSHIP_DOT_READ = 'departmentmembership.read'
    DEPARTMENTMEMBERSHIP_DOT_UPDATE = 'departmentmembership.update'
    EMPLOYEE_DOT_CREATE = 'employee.create'
    EMPLOYEE_DOT_DELETE = 'employee.delete'
    EMPLOYEE_DOT_READ = 'employee.read'
    EMPLOYEE_DOT_UPDATE = 'employee.update'
    FEATURE_DOT_CREATE = 'feature.create'
    FEATURE_DOT_DELETE = 'feature.delete'
    FEATURE_DOT_READ = 'feature.read'
    FEATURE_DOT_UPDATE = 'feature.update'
    FEATUREACCESS_DOT_CREATE = 'featureaccess.create'
    FEATUREACCESS_DOT_DELETE = 'featureaccess.delete'
    FEATUREACCESS_DOT_READ = 'featureaccess.read'
    FEATUREACCESS_DOT_UPDATE = 'featureaccess.update'
    GROUP_DOT_CREATE = 'group.create'
    GROUP_DOT_DELETE = 'group.delete'
    GROUP_DOT_READ = 'group.read'
    GROUP_DOT_UPDATE = 'group.update'
    GROUPRESULT_DOT_CREATE = 'groupresult.create'
    GROUPRESULT_DOT_DELETE = 'groupresult.delete'
    GROUPRESULT_DOT_READ = 'groupresult.read'
    GROUPRESULT_DOT_UPDATE = 'groupresult.update'
    KEY_DOT_CREATE = 'key.create'
    KEY_DOT_DELETE = 'key.delete'
    KEY_DOT_READ = 'key.read'
    KEY_DOT_UPDATE = 'key.update'
    KEYCLOAKWEBHOOK_DOT_CREATE = 'keycloakwebhook.create'
    KEYCLOAKWEBHOOK_DOT_DELETE = 'keycloakwebhook.delete'
    KEYCLOAKWEBHOOK_DOT_READ = 'keycloakwebhook.read'
    KEYCLOAKWEBHOOK_DOT_UPDATE = 'keycloakwebhook.update'
    KEYPAIR_DOT_CREATE = 'keypair.create'
    KEYPAIR_DOT_DELETE = 'keypair.delete'
    KEYPAIR_DOT_READ = 'keypair.read'
    KEYPAIR_DOT_UPDATE = 'keypair.update'
    LOGENTRY_DOT_CREATE = 'logentry.create'
    LOGENTRY_DOT_DELETE = 'logentry.delete'
    LOGENTRY_DOT_READ = 'logentry.read'
    LOGENTRY_DOT_UPDATE = 'logentry.update'
    METEREDALERT_DOT_CREATE = 'meteredalert.create'
    METEREDALERT_DOT_DELETE = 'meteredalert.delete'
    METEREDALERT_DOT_READ = 'meteredalert.read'
    METEREDALERT_DOT_UPDATE = 'meteredalert.update'
    METEREDSERVICE_DOT_CREATE = 'meteredservice.create'
    METEREDSERVICE_DOT_DELETE = 'meteredservice.delete'
    METEREDSERVICE_DOT_READ = 'meteredservice.read'
    METEREDSERVICE_DOT_UPDATE = 'meteredservice.update'
    METERENTRY_DOT_CREATE = 'meterentry.create'
    METERENTRY_DOT_DELETE = 'meterentry.delete'
    METERENTRY_DOT_READ = 'meterentry.read'
    METERENTRY_DOT_UPDATE = 'meterentry.update'
    METERENTRYGROUP_DOT_CREATE = 'meterentrygroup.create'
    METERENTRYGROUP_DOT_DELETE = 'meterentrygroup.delete'
    METERENTRYGROUP_DOT_READ = 'meterentrygroup.read'
    METERENTRYGROUP_DOT_UPDATE = 'meterentrygroup.update'
    NOTIFICATION_DOT_CREATE = 'notification.create'
    NOTIFICATION_DOT_DELETE = 'notification.delete'
    NOTIFICATION_DOT_READ = 'notification.read'
    NOTIFICATION_DOT_UPDATE = 'notification.update'
    NOTIFICATIONCHANNEL_DOT_CREATE = 'notificationchannel.create'
    NOTIFICATIONCHANNEL_DOT_DELETE = 'notificationchannel.delete'
    NOTIFICATIONCHANNEL_DOT_READ = 'notificationchannel.read'
    NOTIFICATIONCHANNEL_DOT_UPDATE = 'notificationchannel.update'
    OAUTH2EVENT_DOT_CREATE = 'oauth2event.create'
    OAUTH2EVENT_DOT_DELETE = 'oauth2event.delete'
    OAUTH2EVENT_DOT_READ = 'oauth2event.read'
    OAUTH2EVENT_DOT_UPDATE = 'oauth2event.update'
    OAUTHSTATETOKEN_DOT_CREATE = 'oauthstatetoken.create'
    OAUTHSTATETOKEN_DOT_DELETE = 'oauthstatetoken.delete'
    OAUTHSTATETOKEN_DOT_READ = 'oauthstatetoken.read'
    OAUTHSTATETOKEN_DOT_UPDATE = 'oauthstatetoken.update'
    OAUTHTOKEN_DOT_CREATE = 'oauthtoken.create'
    OAUTHTOKEN_DOT_DELETE = 'oauthtoken.delete'
    OAUTHTOKEN_DOT_READ = 'oauthtoken.read'
    OAUTHTOKEN_DOT_UPDATE = 'oauthtoken.update'
    PERMISSION_DOT_CREATE = 'permission.create'
    PERMISSION_DOT_DELETE = 'permission.delete'
    PERMISSION_DOT_READ = 'permission.read'
    PERMISSION_DOT_UPDATE = 'permission.update'
    PLAIDLINKTOKEN_DOT_CREATE = 'plaidlinktoken.create'
    PLAIDLINKTOKEN_DOT_DELETE = 'plaidlinktoken.delete'
    PLAIDLINKTOKEN_DOT_READ = 'plaidlinktoken.read'
    PLAIDLINKTOKEN_DOT_UPDATE = 'plaidlinktoken.update'
    PLAIDSYNCTOKEN_DOT_CREATE = 'plaidsynctoken.create'
    PLAIDSYNCTOKEN_DOT_DELETE = 'plaidsynctoken.delete'
    PLAIDSYNCTOKEN_DOT_READ = 'plaidsynctoken.read'
    PLAIDSYNCTOKEN_DOT_UPDATE = 'plaidsynctoken.update'
    PLAN_DOT_CREATE = 'plan.create'
    PLAN_DOT_DELETE = 'plan.delete'
    PLAN_DOT_READ = 'plan.read'
    PLAN_DOT_UPDATE = 'plan.update'
    PRODUCT_DOT_CREATE = 'product.create'
    PRODUCT_DOT_DELETE = 'product.delete'
    PRODUCT_DOT_READ = 'product.read'
    PRODUCT_DOT_UPDATE = 'product.update'
    PROMPTCACHE_DOT_CREATE = 'promptcache.create'
    PROMPTCACHE_DOT_DELETE = 'promptcache.delete'
    PROMPTCACHE_DOT_READ = 'promptcache.read'
    PROMPTCACHE_DOT_UPDATE = 'promptcache.update'
    REQUESTLOG_DOT_CREATE = 'requestlog.create'
    REQUESTLOG_DOT_DELETE = 'requestlog.delete'
    REQUESTLOG_DOT_READ = 'requestlog.read'
    REQUESTLOG_DOT_UPDATE = 'requestlog.update'
    SESSION_DOT_CREATE = 'session.create'
    SESSION_DOT_DELETE = 'session.delete'
    SESSION_DOT_READ = 'session.read'
    SESSION_DOT_UPDATE = 'session.update'
    STRIPEWEBHOOK_DOT_CREATE = 'stripewebhook.create'
    STRIPEWEBHOOK_DOT_DELETE = 'stripewebhook.delete'
    STRIPEWEBHOOK_DOT_READ = 'stripewebhook.read'
    STRIPEWEBHOOK_DOT_UPDATE = 'stripewebhook.update'
    TAG_DOT_CREATE = 'tag.create'
    TAG_DOT_DELETE = 'tag.delete'
    TAG_DOT_READ = 'tag.read'
    TAG_DOT_UPDATE = 'tag.update'
    TAGGEDITEM_DOT_CREATE = 'taggeditem.create'
    TAGGEDITEM_DOT_DELETE = 'taggeditem.delete'
    TAGGEDITEM_DOT_READ = 'taggeditem.read'
    TAGGEDITEM_DOT_UPDATE = 'taggeditem.update'
    TAGTHOUGH_DOT_CREATE = 'tagthough.create'
    TAGTHOUGH_DOT_DELETE = 'tagthough.delete'
    TAGTHOUGH_DOT_READ = 'tagthough.read'
    TAGTHOUGH_DOT_UPDATE = 'tagthough.update'
    TASKRESULT_DOT_CREATE = 'taskresult.create'
    TASKRESULT_DOT_DELETE = 'taskresult.delete'
    TASKRESULT_DOT_READ = 'taskresult.read'
    TASKRESULT_DOT_UPDATE = 'taskresult.update'
    TESTEREMAIL_DOT_CREATE = 'testeremail.create'
    TESTEREMAIL_DOT_DELETE = 'testeremail.delete'
    TESTEREMAIL_DOT_READ = 'testeremail.read'
    TESTEREMAIL_DOT_UPDATE = 'testeremail.update'
    TOOL_DOT_CREATE = 'tool.create'
    TOOL_DOT_DELETE = 'tool.delete'
    TOOL_DOT_READ = 'tool.read'
    TOOL_DOT_UPDATE = 'tool.update'
    TOOLACCESS_DOT_CREATE = 'toolaccess.create'
    TOOLACCESS_DOT_DELETE = 'toolaccess.delete'
    TOOLACCESS_DOT_READ = 'toolaccess.read'
    TOOLACCESS_DOT_UPDATE = 'toolaccess.update'
    TOOLCATEGORY_DOT_CREATE = 'toolcategory.create'
    TOOLCATEGORY_DOT_DELETE = 'toolcategory.delete'
    TOOLCATEGORY_DOT_READ = 'toolcategory.read'
    TOOLCATEGORY_DOT_UPDATE = 'toolcategory.update'
    TOOLUSERACCESS_DOT_CREATE = 'tooluseraccess.create'
    TOOLUSERACCESS_DOT_DELETE = 'tooluseraccess.delete'
    TOOLUSERACCESS_DOT_READ = 'tooluseraccess.read'
    TOOLUSERACCESS_DOT_UPDATE = 'tooluseraccess.update'
    TRANSACTION_DOT_CREATE = 'transaction.create'
    TRANSACTION_DOT_DELETE = 'transaction.delete'
    TRANSACTION_DOT_READ = 'transaction.read'
    TRANSACTION_DOT_UPDATE = 'transaction.update'
    USER_DOT_CREATE = 'user.create'
    USER_DOT_DELETE = 'user.delete'
    USER_DOT_READ = 'user.read'
    USER_DOT_UPDATE = 'user.update'
    USERLICENSE_DOT_CREATE = 'userlicense.create'
    USERLICENSE_DOT_DELETE = 'userlicense.delete'
    USERLICENSE_DOT_READ = 'userlicense.read'
    USERLICENSE_DOT_UPDATE = 'userlicense.update'
    OPENAPI = 'openapi'
    USER_DOT_ME = 'user.me'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PermissionEnum from a JSON string"""
        return cls(json.loads(json_str))


