from twilio.rest import TwilioRestClient

account_sid = 'AC979ad3813e20ecdc20319b7fe1136ad9'
auth_token = 'b1e3c5b91e78739aa720af03f14c70af'

client = TwilioRestClient(account_sid, auth_token)

def send_gas_detected(gas="NONE"):
    gas_found = client.messages.create(
        to = '+15167761919',
        from_ = '+15168745859',
        body = 'GAS LEAK DETECTED ON SENSOR: ' + gas + '. Call the National Gas Service Emergency Line on 0800 111 999 to report a suspected gas leak.')
