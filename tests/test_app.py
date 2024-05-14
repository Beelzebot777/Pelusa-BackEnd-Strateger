import unittest
from flask import Flask, request, jsonify
from datetime import datetime
import json
import sqlite3

# Suponiendo que tu aplicación está en app.py, importa tu app aquí
from app import app, extract_variables, init_db

class WebhookTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        init_db()  # Initialize the database

    def test_webhook_json(self):
        test_data = {
            "Ticker": "BTCUSD",
            "Temporalidad": "1",
            "Exit Price Alert": "62720.62",
            "Time Alert": "18:51:0_13/5/2024",
            "Order": "Close Long",
            "Strategy": "Stochastic_v1"
        }
        response = self.app.post('/webhook', json=test_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['Ticker'], "BTCUSD")
        self.assertEqual(data['Temporalidad'], "1")
        self.assertEqual(data['Exit Price Alert'], "62720.62")
        self.assertEqual(data['Order'], "Close Long")
        self.assertEqual(data['Strategy'], "Stochastic_v1")

    def test_extract_variables_valid(self):
        test_data = '''{
            "Ticker": "BTCUSD",
            "Temporalidad": "1",
            "Quantity": "0.00797186",
            "Entry Price Alert": "62720.62",
            "Time Alert": "18:51:0_13/5/2024",
            "Order": "OpenShort",
            "Strategy": "Stochastic_v1"
        }'''
        expected_result = {
            "Ticker": "BTCUSD",
            "Temporalidad": "1",
            "Quantity": "0.00797186",
            "Entry Price Alert": "62720.62",
            "Exit Price Alert": None,
            "Time Alert": datetime.strptime("18:51:0 13/5/2024", '%H:%M:%S %d/%m/%Y'),
            "Order": "OpenShort",
            "Strategy": "Stochastic_v1"
        }
        result = extract_variables(test_data)
        self.assertIsNotNone(result)
        self.assertEqual(result['Ticker'], expected_result['Ticker'])
        self.assertEqual(result['Temporalidad'], expected_result['Temporalidad'])
        self.assertEqual(result['Quantity'], expected_result['Quantity'])
        self.assertEqual(result['Entry Price Alert'], expected_result['Entry Price Alert'])
        self.assertEqual(result['Time Alert'], expected_result['Time Alert'])
        self.assertEqual(result['Order'], expected_result['Order'])
        self.assertEqual(result['Strategy'], expected_result['Strategy'])

    def test_extract_variables_invalid_json(self):
        invalid_json_data = '''Ticker: BTCUSD, Temporalidad: 1, Quantity: 0.00797186, Entry Price Alert: 62720.62, Time Alert: 18:51:0_13/5/2024, Order: OpenShort, Strategy: Stochastic_v1'''
        result = extract_variables(invalid_json_data)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
