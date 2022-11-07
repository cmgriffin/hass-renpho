from datetime import timedelta

"""Constants for constants sake"""

DOMAIN = "renpho_weight"

CONF_EMAIL = 'email'
CONF_PASSWORD = 'password'
CONF_REFRESH = 'refresh'
CONF_WEIGHT_UNITS = 'weight_units'

DEFAULT_CONF_WEIGHT_UNITS = 'kg'
DEFAULT_CONF_REFRESH = timedelta(hours=3)

KG_TO_LB_MULTIPLICATOR = 2.2046226218

CONF_PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+25I2upukpfQ7rIaaTZtVE744\nu2zV+HaagrUhDOTq8fMVf9yFQvEZh2/HKxFudUxP0dXUa8F6X4XmWumHdQnum3zm\nJr04fz2b2WCcN0ta/rbF2nYAnMVAk2OJVZAMudOiMWhcxV1nNJiKgTNNr13de0EQ\nIiOL2CUBzu+HmIfUbQIDAQAB\n-----END PUBLIC KEY-----'