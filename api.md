# Archives

Methods:

- <code title="delete /v1/Archives/{Date}/Calls/{Sid}">client.archives.<a href="./src/twilio_voice_openapi/resources/archives.py">delete_call</a>(sid, \*, date) -> None</code>

# ByocTrunks

Types:

```python
from twilio_voice_openapi.types import ByocTrunk, ByocTrunkListResponse
```

Methods:

- <code title="post /v1/ByocTrunks">client.byoc_trunks.<a href="./src/twilio_voice_openapi/resources/byoc_trunks.py">create</a>(\*\*<a href="src/twilio_voice_openapi/types/byoc_trunk_create_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/byoc_trunk.py">ByocTrunk</a></code>
- <code title="get /v1/ByocTrunks/{Sid}">client.byoc_trunks.<a href="./src/twilio_voice_openapi/resources/byoc_trunks.py">retrieve</a>(sid) -> <a href="./src/twilio_voice_openapi/types/byoc_trunk.py">ByocTrunk</a></code>
- <code title="post /v1/ByocTrunks/{Sid}">client.byoc_trunks.<a href="./src/twilio_voice_openapi/resources/byoc_trunks.py">update</a>(sid, \*\*<a href="src/twilio_voice_openapi/types/byoc_trunk_update_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/byoc_trunk.py">ByocTrunk</a></code>
- <code title="get /v1/ByocTrunks">client.byoc_trunks.<a href="./src/twilio_voice_openapi/resources/byoc_trunks.py">list</a>(\*\*<a href="src/twilio_voice_openapi/types/byoc_trunk_list_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/byoc_trunk_list_response.py">ByocTrunkListResponse</a></code>
- <code title="delete /v1/ByocTrunks/{Sid}">client.byoc_trunks.<a href="./src/twilio_voice_openapi/resources/byoc_trunks.py">delete</a>(sid) -> None</code>

# ConnectionPolicies

Types:

```python
from twilio_voice_openapi.types import ConnectionPolicy, ConnectionPolicyListResponse
```

Methods:

- <code title="post /v1/ConnectionPolicies">client.connection_policies.<a href="./src/twilio_voice_openapi/resources/connection_policies/connection_policies.py">create</a>(\*\*<a href="src/twilio_voice_openapi/types/connection_policy_create_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/connection_policy.py">ConnectionPolicy</a></code>
- <code title="get /v1/ConnectionPolicies/{Sid}">client.connection_policies.<a href="./src/twilio_voice_openapi/resources/connection_policies/connection_policies.py">retrieve</a>(sid) -> <a href="./src/twilio_voice_openapi/types/connection_policy.py">ConnectionPolicy</a></code>
- <code title="post /v1/ConnectionPolicies/{Sid}">client.connection_policies.<a href="./src/twilio_voice_openapi/resources/connection_policies/connection_policies.py">update</a>(sid, \*\*<a href="src/twilio_voice_openapi/types/connection_policy_update_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/connection_policy.py">ConnectionPolicy</a></code>
- <code title="get /v1/ConnectionPolicies">client.connection_policies.<a href="./src/twilio_voice_openapi/resources/connection_policies/connection_policies.py">list</a>(\*\*<a href="src/twilio_voice_openapi/types/connection_policy_list_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/connection_policy_list_response.py">ConnectionPolicyListResponse</a></code>
- <code title="delete /v1/ConnectionPolicies/{Sid}">client.connection_policies.<a href="./src/twilio_voice_openapi/resources/connection_policies/connection_policies.py">delete</a>(sid) -> None</code>

## Targets

Types:

```python
from twilio_voice_openapi.types.connection_policies import (
    ConnectionPolicyTarget,
    TargetListResponse,
)
```

Methods:

- <code title="post /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets">client.connection_policies.targets.<a href="./src/twilio_voice_openapi/resources/connection_policies/targets.py">create</a>(connection_policy_sid, \*\*<a href="src/twilio_voice_openapi/types/connection_policies/target_create_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/connection_policies/connection_policy_target.py">ConnectionPolicyTarget</a></code>
- <code title="get /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid}">client.connection_policies.targets.<a href="./src/twilio_voice_openapi/resources/connection_policies/targets.py">retrieve</a>(sid, \*, connection_policy_sid) -> <a href="./src/twilio_voice_openapi/types/connection_policies/connection_policy_target.py">ConnectionPolicyTarget</a></code>
- <code title="post /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid}">client.connection_policies.targets.<a href="./src/twilio_voice_openapi/resources/connection_policies/targets.py">update</a>(sid, \*, connection_policy_sid, \*\*<a href="src/twilio_voice_openapi/types/connection_policies/target_update_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/connection_policies/connection_policy_target.py">ConnectionPolicyTarget</a></code>
- <code title="get /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets">client.connection_policies.targets.<a href="./src/twilio_voice_openapi/resources/connection_policies/targets.py">list</a>(connection_policy_sid, \*\*<a href="src/twilio_voice_openapi/types/connection_policies/target_list_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/connection_policies/target_list_response.py">TargetListResponse</a></code>
- <code title="delete /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid}">client.connection_policies.targets.<a href="./src/twilio_voice_openapi/resources/connection_policies/targets.py">delete</a>(sid, \*, connection_policy_sid) -> None</code>

# DialingPermissions

Types:

```python
from twilio_voice_openapi.types import DialingPermissionCreateBulkCountryUpdatesResponse
```

Methods:

- <code title="post /v1/DialingPermissions/BulkCountryUpdates">client.dialing_permissions.<a href="./src/twilio_voice_openapi/resources/dialing_permissions/dialing_permissions.py">create_bulk_country_updates</a>(\*\*<a href="src/twilio_voice_openapi/types/dialing_permission_create_bulk_country_updates_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/dialing_permission_create_bulk_country_updates_response.py">DialingPermissionCreateBulkCountryUpdatesResponse</a></code>

## Countries

Types:

```python
from twilio_voice_openapi.types.dialing_permissions import (
    CountryRetrieveResponse,
    CountryListResponse,
    CountryFetchHighRiskSpecialPrefixesResponse,
)
```

Methods:

- <code title="get /v1/DialingPermissions/Countries/{IsoCode}">client.dialing_permissions.countries.<a href="./src/twilio_voice_openapi/resources/dialing_permissions/countries.py">retrieve</a>(iso_code) -> <a href="./src/twilio_voice_openapi/types/dialing_permissions/country_retrieve_response.py">CountryRetrieveResponse</a></code>
- <code title="get /v1/DialingPermissions/Countries">client.dialing_permissions.countries.<a href="./src/twilio_voice_openapi/resources/dialing_permissions/countries.py">list</a>(\*\*<a href="src/twilio_voice_openapi/types/dialing_permissions/country_list_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/dialing_permissions/country_list_response.py">CountryListResponse</a></code>
- <code title="get /v1/DialingPermissions/Countries/{IsoCode}/HighRiskSpecialPrefixes">client.dialing_permissions.countries.<a href="./src/twilio_voice_openapi/resources/dialing_permissions/countries.py">fetch_high_risk_special_prefixes</a>(iso_code, \*\*<a href="src/twilio_voice_openapi/types/dialing_permissions/country_fetch_high_risk_special_prefixes_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/dialing_permissions/country_fetch_high_risk_special_prefixes_response.py">CountryFetchHighRiskSpecialPrefixesResponse</a></code>

# Settings

Types:

```python
from twilio_voice_openapi.types import DialingPermissions
```

Methods:

- <code title="get /v1/Settings">client.settings.<a href="./src/twilio_voice_openapi/resources/settings.py">retrieve</a>() -> <a href="./src/twilio_voice_openapi/types/dialing_permissions.py">DialingPermissions</a></code>
- <code title="post /v1/Settings">client.settings.<a href="./src/twilio_voice_openapi/resources/settings.py">update</a>(\*\*<a href="src/twilio_voice_openapi/types/setting_update_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/dialing_permissions.py">DialingPermissions</a></code>

# IPRecords

Types:

```python
from twilio_voice_openapi.types import IPRecord, IPRecordListResponse
```

Methods:

- <code title="post /v1/IpRecords">client.ip_records.<a href="./src/twilio_voice_openapi/resources/ip_records.py">create</a>(\*\*<a href="src/twilio_voice_openapi/types/ip_record_create_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/ip_record.py">IPRecord</a></code>
- <code title="get /v1/IpRecords/{Sid}">client.ip_records.<a href="./src/twilio_voice_openapi/resources/ip_records.py">retrieve</a>(sid) -> <a href="./src/twilio_voice_openapi/types/ip_record.py">IPRecord</a></code>
- <code title="post /v1/IpRecords/{Sid}">client.ip_records.<a href="./src/twilio_voice_openapi/resources/ip_records.py">update</a>(sid, \*\*<a href="src/twilio_voice_openapi/types/ip_record_update_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/ip_record.py">IPRecord</a></code>
- <code title="get /v1/IpRecords">client.ip_records.<a href="./src/twilio_voice_openapi/resources/ip_records.py">list</a>(\*\*<a href="src/twilio_voice_openapi/types/ip_record_list_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/ip_record_list_response.py">IPRecordListResponse</a></code>
- <code title="delete /v1/IpRecords/{Sid}">client.ip_records.<a href="./src/twilio_voice_openapi/resources/ip_records.py">delete</a>(sid) -> None</code>

# SourceIPMappings

Types:

```python
from twilio_voice_openapi.types import SourceIPMapping, SourceIPMappingListResponse
```

Methods:

- <code title="post /v1/SourceIpMappings">client.source_ip_mappings.<a href="./src/twilio_voice_openapi/resources/source_ip_mappings.py">create</a>(\*\*<a href="src/twilio_voice_openapi/types/source_ip_mapping_create_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/source_ip_mapping.py">SourceIPMapping</a></code>
- <code title="get /v1/SourceIpMappings/{Sid}">client.source_ip_mappings.<a href="./src/twilio_voice_openapi/resources/source_ip_mappings.py">retrieve</a>(sid) -> <a href="./src/twilio_voice_openapi/types/source_ip_mapping.py">SourceIPMapping</a></code>
- <code title="post /v1/SourceIpMappings/{Sid}">client.source_ip_mappings.<a href="./src/twilio_voice_openapi/resources/source_ip_mappings.py">update</a>(sid, \*\*<a href="src/twilio_voice_openapi/types/source_ip_mapping_update_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/source_ip_mapping.py">SourceIPMapping</a></code>
- <code title="get /v1/SourceIpMappings">client.source_ip_mappings.<a href="./src/twilio_voice_openapi/resources/source_ip_mappings.py">list</a>(\*\*<a href="src/twilio_voice_openapi/types/source_ip_mapping_list_params.py">params</a>) -> <a href="./src/twilio_voice_openapi/types/source_ip_mapping_list_response.py">SourceIPMappingListResponse</a></code>
- <code title="delete /v1/SourceIpMappings/{Sid}">client.source_ip_mappings.<a href="./src/twilio_voice_openapi/resources/source_ip_mappings.py">delete</a>(sid) -> None</code>
