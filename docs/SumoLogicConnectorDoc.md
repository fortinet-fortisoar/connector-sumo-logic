## About the connector
Sumo Logic connector provides application collect and analyze machine data
<p>This document provides information about the Sumo Logic Connector, which facilitates automated interactions, with a Sumo Logic server using FortiSOAR&trade; playbooks. Add the Sumo Logic Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Sumo Logic.</p>

### Version information

Connector Version: 1.1.0


Authored By: SpryIQ.Co

Certified: No
## Release Notes for version 1.1.0
Following enhancements have been made to the Sumo Logic Connector in version 1.1.0:
<h2>What's Fixed</h2>

<h3>Added Operations:</h3>

<ul>
<li>Get the List of Insights By Query</li>
<li>Get the List of All Insights</li>
<li>Get Details By Insights ID</li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-sumo-logic</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Sumo Logic server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Sumo Logic server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Sumo Logic</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>URL of the Sumo Logic API server to which you will connect and perform automated operations.
</td>
</tr><tr><td>Access ID</td><td>ID required to access the Sumo Logic API.
</td>
</tr><tr><td>Access Key</td><td>Key to access the Sumo Logic API.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Search Job</td><td>Creates a search job based on the specified query and time range in Sumo Logic.</td><td>create_search_job <br/>Investigation</td></tr>
<tr><td>Get Search Job Status</td><td>Retrieves the current status of a search job from Sumo Logic based on the search job ID you have specified.</td><td>get_search_job_status <br/>Investigation</td></tr>
<tr><td>Get Messages Founded by Search Job</td><td>Retrieves messages found by a search job from Sumo Logic based on the search job ID, offset, and limit you have specified.</td><td>get_messages_founded_by_search_job <br/>Investigation</td></tr>
<tr><td>Get Records Founded by Search Job</td><td>Retrieves records found by a search job from Sumo Logic based on the search job ID, offset, and limit you have specified.</td><td>get_records_founded_by_search_job <br/>Investigation</td></tr>
<tr><td>Delete Search Job</td><td>Deletes a search job from Sumo Logic based on the search job ID you have specified.</td><td>delete_search_job <br/>Investigation</td></tr>
<tr><td>Get the List of All Insights</td><td>Note: This API will not return more than 10,000 Signals for a given query, even when split over many pages. To retrieve all Signals, use the /signals/all API.</td><td>get_list_of_all_insights <br/>Investigation</td></tr>
<tr><td>Get Details By Insights ID</td><td>Note: This API will not return more than 10,000 Signals for a given query, even when split over many pages. To retrieve all Signals, use the /signals/all API.</td><td>get_details_by_insights_id <br/>Investigation</td></tr>
<tr><td>Get the List of Insights By Query</td><td>Note: This API will not return more than 10,000 Signals for a given query, even when split over many pages. To retrieve all Signals, use the /signals/all API.</td><td>get_list_of_insights_by_query <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Search Job
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>Query using which you want to create and execute a seach job in Sumo Logic. 
Note: You must add this query in a valid JSON format.
</td></tr><tr><td>From</td><td>Start date and time from which you want to start the search in Sumo Logic. The date must be in the YYYY-MM-DDTHH:mm:ss format.
</td></tr><tr><td>To</td><td>End date and time till when you want to end the search in Sumo Logic. The date must be in the YYYY-MM-DDTHH:mm:ss format.
</td></tr><tr><td>Time Zone</td><td>Select the timezone in which you want to start the search in Sumo Logic.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "link": {
        "rel": "",
        "href": ""
    }
}</pre>

### operation: Get Search Job Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search Job ID</td><td>ID of the search job whose status you want to retrieve from Sumo Logic.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "state": "",
    "histogramBuckets": [
        {
            "startTimestamp": "",
            "length": "",
            "count": ""
        }
    ],
    "messageCount": "",
    "recordCount": "",
    "pendingWarnings": [],
    "pendingErrors": [],
    "usageDetails": ""
}</pre>

### operation: Get Messages Founded by Search Job
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search Job ID</td><td>ID of the search job whose messages you want to retrieve from Sumo Logic.
</td></tr><tr><td>Offset</td><td>Index of the first item to be returned by this operation. This parameter is useful if you want to get a subset of records, say messages starting from the 10th message. By default, this is set as 0.
</td></tr><tr><td>Limit</td><td>Maximum number of messages, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "fields": [
        {
            "name": "",
            "fieldType": "",
            "keyField": ""
        }
    ],
    "messages": [
        {
            "map": {
                "_collector": "",
                "eventtime": "",
                "type": "",
                "eventsource": "",
                "_messageid": "",
                "_size": "",
                "accountid": "",
                "category_string": "",
                "event_type": "",
                "action": "",
                "awsaccountid": "",
                "eventversion": "",
                "groupid": "",
                "_sourceid": "",
                "cidr_block": "",
                "requestid": "",
                "_source": "",
                "eventtype": "",
                "from_port": "",
                "eventid": "",
                "_raw": "",
                "_collectorid": "",
                "useragent": "",
                "_sourcehost": "",
                "eventname": "",
                "accesskeyid": "",
                "egress": "",
                "computer": "",
                "logon_id": "",
                "msg_summary": "",
                "account_name": "",
                "_format": "",
                "arn": "",
                "_blockid": "",
                "sourceipaddress": "",
                "account_domain": "",
                "_messagetime": "",
                "to_port": "",
                "_messagecount": "",
                "principalid": "",
                "recipientaccountid": "",
                "_sourcename": "",
                "event_id": "",
                "_view": "",
                "_receipttime": "",
                "_sourcecategory": "",
                "category": "",
                "responseelements": "",
                "awsregion": "",
                "username": ""
            }
        }
    ]
}</pre>

### operation: Get Records Founded by Search Job
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search Job ID</td><td>ID of the search job whose records you want to retrieve from Sumo Logic.
</td></tr><tr><td>Offset</td><td>Index of the first item to be returned by this operation. This parameter is useful if you want to get a subset of records, say records starting from the 10th record. By default, this is set as 0.
</td></tr><tr><td>Limit</td><td>Maximum number of messages, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "fields": [
        {
            "name": "",
            "fieldType": "",
            "keyField": ""
        }
    ],
    "records": [
        {
            "map": {
                "_count": "",
                "_sourcecategory": ""
            }
        }
    ]
}</pre>

### operation: Delete Search Job
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search Job ID</td><td>ID of the search job that you want to delete from Sumo Logic.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": ""
}</pre>

### operation: Get the List of All Insights
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "fields": [
        {
            "name": "",
            "fieldType": "",
            "keyField": ""
        }
    ],
    "records": [
        {
            "map": {
                "_count": "",
                "_sourcecategory": ""
            }
        }
    ]
}</pre>

### operation: Get Details By Insights ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Insights ID</td><td>ID of the search insights that you want to retrieve from Sumo Logic.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "fields": [
        {
            "name": "",
            "fieldType": "",
            "keyField": ""
        }
    ],
    "records": [
        {
            "map": {
                "_count": "",
                "_sourcecategory": ""
            }
        }
    ]
}</pre>

### operation: Get the List of Insights By Query
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>Query of the search insights that you want to retrieve from Sumo Logic.
</td></tr><tr><td>Offset</td><td>Index of the first item to be returned by this operation. This parameter is useful if you want to get a subset of records, say records starting from the 10th record. By default, this is set as 0.
</td></tr><tr><td>Limit</td><td>Maximum number of messages, per page, that this operation should return.
</td></tr><tr><td>Record Summary Fields</td><td>Specify the record summary field
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "fields": [
        {
            "name": "",
            "fieldType": "",
            "keyField": ""
        }
    ],
    "records": [
        {
            "map": {
                "_count": "",
                "_sourcecategory": ""
            }
        }
    ]
}</pre>
## Included playbooks
The `Sample - sumo-logic - 1.1.0` playbook collection comes bundled with the Sumo Logic connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Sumo Logic connector.

- Create Search Job
- Delete Search Job
- Get Details By Insights ID
- Get Messages Founded by Search Job
- Get Records Founded by Search Job
- Get Search Job Status
- Get the List of All Insights
- Get the List of Insights By Query

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
