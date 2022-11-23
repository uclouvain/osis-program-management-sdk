# osis_program_management_sdk.TrainingsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/program_management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**training_prerequisites_official**](TrainingsApi.md#training_prerequisites_official) | **GET** /trainings/{year}/{acronym}/prerequisites | 
[**training_prerequisites_transition**](TrainingsApi.md#training_prerequisites_transition) | **GET** /trainings/{year}/{acronym}/transition/prerequisites | 
[**training_prerequisites_version**](TrainingsApi.md#training_prerequisites_version) | **GET** /trainings/{year}/{acronym}/{version_name}/prerequisites | 
[**training_prerequisites_version_transition**](TrainingsApi.md#training_prerequisites_version_transition) | **GET** /trainings/{year}/{acronym}/{version_name}/transition/prerequisites | 


# **training_prerequisites_official**
> ArrayOfProgramTreePrerequisites training_prerequisites_official(year, acronym)



Return the prerequisites of the learning units of the training (standard version)

### Example

* Api Key Authentication (Token):

```python
import time
import osis_program_management_sdk
from osis_program_management_sdk.api import trainings_api
from osis_program_management_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_program_management_sdk.model.error import Error
from osis_program_management_sdk.model.array_of_program_tree_prerequisites import ArrayOfProgramTreePrerequisites
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/program_management
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_program_management_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/program_management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_program_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.training_prerequisites_official(year, acronym)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_official: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.training_prerequisites_official(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_official: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ArrayOfProgramTreePrerequisites**](ArrayOfProgramTreePrerequisites.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **training_prerequisites_transition**
> ArrayOfProgramTreePrerequisites training_prerequisites_transition(year, acronym)



Return the prerequisites of the learning units of the training (standard version transition)

### Example

* Api Key Authentication (Token):

```python
import time
import osis_program_management_sdk
from osis_program_management_sdk.api import trainings_api
from osis_program_management_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_program_management_sdk.model.error import Error
from osis_program_management_sdk.model.array_of_program_tree_prerequisites import ArrayOfProgramTreePrerequisites
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/program_management
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_program_management_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/program_management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_program_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.training_prerequisites_transition(year, acronym)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_transition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.training_prerequisites_transition(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_transition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ArrayOfProgramTreePrerequisites**](ArrayOfProgramTreePrerequisites.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **training_prerequisites_version**
> ArrayOfProgramTreePrerequisites training_prerequisites_version(year, acronym, version_name)



Return the prerequisites of the learning units of the training version

### Example

* Api Key Authentication (Token):

```python
import time
import osis_program_management_sdk
from osis_program_management_sdk.api import trainings_api
from osis_program_management_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_program_management_sdk.model.error import Error
from osis_program_management_sdk.model.array_of_program_tree_prerequisites import ArrayOfProgramTreePrerequisites
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/program_management
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_program_management_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/program_management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_program_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    version_name = "version_name_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.training_prerequisites_version(year, acronym, version_name)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.training_prerequisites_version(year, acronym, version_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **version_name** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ArrayOfProgramTreePrerequisites**](ArrayOfProgramTreePrerequisites.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **training_prerequisites_version_transition**
> ArrayOfProgramTreePrerequisites training_prerequisites_version_transition(year, acronym, version_name)



Return the prerequisites of the learning units of the training version (transition)

### Example

* Api Key Authentication (Token):

```python
import time
import osis_program_management_sdk
from osis_program_management_sdk.api import trainings_api
from osis_program_management_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_program_management_sdk.model.error import Error
from osis_program_management_sdk.model.array_of_program_tree_prerequisites import ArrayOfProgramTreePrerequisites
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/program_management
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_program_management_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/program_management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_program_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trainings_api.TrainingsApi(api_client)
    year = "year_example" # str | 
    acronym = "acronym_example" # str | 
    version_name = "version_name_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.training_prerequisites_version_transition(year, acronym, version_name)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_version_transition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.training_prerequisites_version_transition(year, acronym, version_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_program_management_sdk.ApiException as e:
        print("Exception when calling TrainingsApi->training_prerequisites_version_transition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **acronym** | **str**|  |
 **version_name** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ArrayOfProgramTreePrerequisites**](ArrayOfProgramTreePrerequisites.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

