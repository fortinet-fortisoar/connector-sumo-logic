"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import check_health, sumo_logic_ops

logger = get_logger('sumo_logic')

class SumoLogic(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.info('In execute() Operation:[{}]'.format(operation))
        operation = sumo_logic_ops.get(operation, None)
        if not operation:
            logger.info('Unsupported operation [{}]'.format(operation))
            raise ConnectorError('Unsupported operation')
        result = operation(config, params)
        return result

    def check_health(self, config):
        return check_health(config)