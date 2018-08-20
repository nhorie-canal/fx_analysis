import http.client
import requests


class Execution(object):
    def __init__(self, domain, access_token, account_id):
        self.domain = domain
        self.access_token = access_token
        self.account_id = account_id
        self.conn = self.obtain_connection()

    def obtain_connection(self):
        return http.client.HTTPSConnection(self.domain)

    def execute_order(self, event):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer " + self.access_token
        }
        params = [
            ('instrument', event.instrument),
            ('units', event.units),
            ('side', event.side),
            ('type', event.order_type),
        ]
        response = requests.post('https://api-fxpractice.oanda.com/v1/accounts/%s/orders' % str(self.account_id),
                                 headers=headers,
                                 data=params)

        print(response)

