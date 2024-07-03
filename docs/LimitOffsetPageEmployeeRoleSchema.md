# LimitOffsetPageEmployeeRoleSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmployeeRoleSchema]**](EmployeeRoleSchema.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from async_anchio.models.limit_offset_page_employee_role_schema import LimitOffsetPageEmployeeRoleSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageEmployeeRoleSchema from a JSON string
limit_offset_page_employee_role_schema_instance = LimitOffsetPageEmployeeRoleSchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageEmployeeRoleSchema.to_json()

# convert the object into a dict
limit_offset_page_employee_role_schema_dict = limit_offset_page_employee_role_schema_instance.to_dict()
# create an instance of LimitOffsetPageEmployeeRoleSchema from a dict
limit_offset_page_employee_role_schema_form_dict = limit_offset_page_employee_role_schema.from_dict(limit_offset_page_employee_role_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


