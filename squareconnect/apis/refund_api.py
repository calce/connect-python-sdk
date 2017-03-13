# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RefundApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_refund(self, location_id, transaction_id, body, **kwargs):
        """
        CreateRefund
        Initiates a refund for a previously charged tender.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_refund(location_id, transaction_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str location_id: The ID of the original transaction's associated location. (required)
        :param str transaction_id: The ID of the original transaction that includes the tender to refund. (required)
        :param CreateRefundRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: CreateRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'transaction_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_refund" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `create_refund`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `create_refund`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_refund`")


        resource_path = '/v2/locations/{location_id}/transactions/{transaction_id}/refund'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']
        if 'transaction_id' in params:
            path_params['transaction_id'] = params['transaction_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateRefundResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def list_refunds(self, location_id, **kwargs):
        """
        ListRefunds
        Lists refunds for one of a business's locations.  Refunds with a `status` of `PENDING` are not currently included in this endpoint's response.  Max results per [page](#paginatingresults): 50

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_refunds(location_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str location_id: The ID of the location to list refunds for. (required)
        :param str begin_time: The beginning of the requested reporting period, in RFC 3339 format.  See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.  Default value: The current time minus one year.
        :param str end_time: The end of the requested reporting period, in RFC 3339 format.  See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.  Default value: The current time.
        :param str sort_order: The order in which results are listed in the response (`ASC` for oldest first, `DESC` for newest first).  Default value: `DESC`
        :param str cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](#paginatingresults) for more information.
        :return: ListRefundsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'begin_time', 'end_time', 'sort_order', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_refunds" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `list_refunds`")


        resource_path = '/v2/locations/{location_id}/refunds'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']

        query_params = {}
        if 'begin_time' in params and params['begin_time'] is not None:
            query_params['begin_time'] = params['begin_time']
        if 'end_time' in params and params['end_time'] is not None:
            query_params['end_time'] = params['end_time']
        if 'sort_order' in params and params['sort_order'] is not None:
            query_params['sort_order'] = params['sort_order']
        if 'cursor' in params and params['cursor'] is not None:
            query_params['cursor'] = params['cursor']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ListRefundsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        
