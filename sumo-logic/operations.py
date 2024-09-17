""" Copyright start
  Copyright (C) 2008 - 2021 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import base64, json, requests
from connectors.core.connector import ConnectorError, get_logger

logger = get_logger('sumo_logic')

SSL_VALIDATION_ERROR = 'SSL certificate validation failed'
CONNECTION_TIMEOUT = 'The request timed out while trying to connect to the remote server'
REQUEST_READ_TIMEOUT = 'The server did not send any data in the allotted amount of time'
CREATE_SEARCH_JOB = '/api/v1/search/jobs'
SEARCH_JOB_STATUS = '/api/v1/search/jobs/{SEARCH_JOB_ID}'
GET_MESSAGE_BY_SEARCH_JOB = '/api/v1/search/jobs/{SEARCH_JOB_ID}/messages?offset={OFFSET}&limit={LIMIT}'
GET_RECORDS_BY_SEARCH_JOB = '/api/v1/search/jobs/{SEARCH_JOB_ID}/records?offset={OFFSET}&limit={LIMIT}'
CHECK = '/api/v1/collectors?limit=2'


ERROR_MSG = {
    400: 'Bad/Invalid Request',
    401: 'Requested resource is unauthorized.',
    402: 'API Search quota is exceeded',
    403: 'This operation is not allowed for your account type.',
    404: 'Requested resource could not be found.',
    500: 'Internal Server Error',
    503: 'Service Unavailable',
    'time_out': 'The request timed out while trying to connect to the remote server',
    'ssl_error': 'SSL certificate validation failed'
}


def _get_input(params, key, type=str):
    ret_val = params.get(key, None)
    if ret_val:
        if isinstance(ret_val, bytes):
            ret_val = ret_val.decode('utf-8')
        if isinstance(ret_val, type):
            return ret_val
        else:
            logger.info(
                "Parameter Input Type is Invalid: Parameter is: {0}, Required Parameter Type"
                " is: {1}".format(str(key), str(type)))
            raise ConnectorError("Parameter Input Type is Invalid: Parameter is: {0}, Required "
                                 "Parameter Type is: {1}".format(str(key), str(type)))
    else:
        if ret_val == {} or ret_val == [] or ret_val == 0:
            return ret_val
        return None


def _get_config(config):
    verify_ssl = config.get("verify_ssl", None)
    server_url = _get_input(config, "server_url")
    access_id = _get_input(config, "access_id")
    access_key = _get_input(config, "access_key")
    return server_url, access_id, access_key, verify_ssl


def _get_token(access_id, access_key):
    try:
        return base64.b64encode('{0}:{1}'.format(access_id, access_key).encode('utf-8')).decode('utf-8')
    except Exception as Err:
        raise ConnectorError(Err)


def _api_request(url, config, method='get', payload={}, json_format=True, params=None):
    try:
        server_url, access_id, access_key, verify_ssl = _get_config(config)
        if not server_url.startswith('https://'):
            server_url = 'https://' + server_url

        token = _get_token(access_id, access_key)
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + token
        }
        request_url = server_url + url
        api_response = requests.request(method=method, url=request_url, headers=header,
                                        data=json.dumps(payload), params=params, verify=verify_ssl)
        if api_response.ok:
            if json_format == True:
                return json.loads(api_response.content.decode('utf-8'))
            else:
                return api_response.content
        elif api_response.status_code in ERROR_MSG:
            raise ConnectorError(ERROR_MSG[api_response.status_code])
        else:
            logger.info('Fail To request API {0} response is : {1}'.format(str(url), str(
                api_response.content)))
            raise ConnectorError('Fail To request API {0} response is :{1}'.format(str(url), str(
                api_response.content)))
    except Exception as Err:
        raise ConnectorError(Err)

def _get_list_from_str_or_list(params, parameter):
    try:
        parameter_list = params.get(parameter)
        if parameter_list:
            if isinstance(parameter_list, str):
                parameter_list = parameter_list.split(",")
                return parameter_list
            elif isinstance(parameter_list, list):
                return parameter_list
        else:
            logger.info("{0} Are Empty: {1}".format(parameter, parameter_list))
            return None
        raise ConnectorError(
            "{0} Are Not in Format or Empty: {1}".format(parameter, parameter_list))
    except Exception as Err:
        raise ConnectorError(Err)

def check_health(config):
    try:
        response = _api_request(CHECK, config)
        if response:
            return True
        else:
            return False
    except requests.exceptions.SSLError:
        raise ConnectorError(SSL_VALIDATION_ERROR)
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError(CONNECTION_TIMEOUT)
    except requests.exceptions.ReadTimeout:
        raise ConnectorError(REQUEST_READ_TIMEOUT)
    except Exception as err:
        raise ConnectorError(str(err))

def create_search_job(config, params):
    try:
        param = {
            "query": _get_input(params, "query"),
            "from": _get_input(params, "from").split()[0][:19],
            "to": _get_input(params, "to").split()[0][:19],
            "timeZone": _get_input(params, "timeZone")
        }
        return _api_request(CREATE_SEARCH_JOB, config, payload=param, method="post")
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_search_job_status(config, params):
    try:
        return _api_request(SEARCH_JOB_STATUS.format(SEARCH_JOB_ID=params.get('searchJobId')), config)
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_messages_founded_by_search_job(config, params):
    try:
        searchJobId = params.get('searchJobId')
        offset = params.get('offset')
        limit = params.get('limit')
        return _api_request(
            GET_MESSAGE_BY_SEARCH_JOB.format(SEARCH_JOB_ID=searchJobId, OFFSET=offset, LIMIT=limit),
            config)
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_records_founded_by_search_job(config, params):
    try:
        searchJobId = params.get('searchJobId')
        offset = params.get('offset')
        limit = params.get('limit')
        return _api_request(
            GET_RECORDS_BY_SEARCH_JOB.format(SEARCH_JOB_ID=searchJobId, OFFSET=offset, LIMIT=limit),
            config)
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def delete_search_job(config, params):
    try:
        searchJobId = params.get('searchJobId')
        return _api_request(SEARCH_JOB_STATUS.format(SEARCH_JOB_ID=searchJobId), config,
                            method='delete')
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_list_of_all_insights(config, params):
    try:
        query = f'/api/sec/v1/insights/all'
        return _api_request(query, config)
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_details_by_insights_id(config, params):
    try:
        insights_id = params.get('insights_id')
        quary = f'/api/sec/v1/insights/{insights_id}'
        return _api_request(quary, config)
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_list_of_insights(config, params):
    try:
        offset = params.get('offset')
        limit = params.get('limit')
        record_summary_fields = params.get('recordSummaryFields').split(',')
        record_summary_fields_str = ','.join(record_summary_fields)
        query = f'/api/sec/v1/insights?offset={offset}&limit={limit}&recordSummaryFields={record_summary_fields_str}'
        return _api_request(query, config)
    except Exception as Err:
        logger.exception(str(Err))
        raise ConnectorError(str(Err))


def get_list_of_insights_by_query(config, params):
    try:
        query = _get_input(params, "query")
        param = {
            "query": query,
        }
        offset = params.get('offset')  # Provide a default value for offset
        limit = params.get('limit')  # Provide a default value for limit

        # Handle recordSummaryFields correctly
        record_summary_fields = params.get('recordSummaryFields', '')
        record_summary_fields_list = record_summary_fields.split(',') if record_summary_fields else []
        record_summary_fields_str = ','.join(record_summary_fields_list)

        query_url = f'/api/sec/v1/insights?offset={offset}&limit={limit}&recordSummaryFields={record_summary_fields_str}'
        return _api_request(query_url, config, payload=param, method='get')
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


sumo_logic_ops = {
    'create_search_job': create_search_job,
    'get_search_job_status': get_search_job_status,
    'get_messages_founded_by_search_job': get_messages_founded_by_search_job,
    'get_records_founded_by_search_job': get_records_founded_by_search_job,
    'delete_search_job': delete_search_job,
    'get_list_of_insights_by_query': get_list_of_insights_by_query,
    'get_list_of_all_insights': get_list_of_all_insights,
    'get_details_by_insights_id': get_details_by_insights_id,
    'get_list_of_insights': get_list_of_insights,
}
