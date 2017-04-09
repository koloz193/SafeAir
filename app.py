from flask import Flask, request, redirect
from twilio import twiml
from gas_detect import get_mq3_level, get_mq5_level, passive_scan

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)

    resp = twiml.Response()

    if (body == "Level of MQ3"):
        m = get_mq3_level()
        m = "Current MQ3 Level is: " + str(m) + "."
        resp.message(m)
    elif (body == "Level of MQ5"):
        m = get_mq5_level()
        m = "Current MQ5 Level is: " + str(m) + "."
        resp.message(m)
    elif (body == "Full Scan"):
        mq3 = get_mq3_level()
        mq5 = get_mq5_level()
        m = "Current MQ3 Level is: " + str(mq3) + ". Current MQ5 Level is: " + str(mq5) + "."
    elif (body == "Passive Scan"):
        gas_detect.passive_scan()
    else:
        resp.message("Reply 'Level of MQ3' | 'Level of MQ5' | 'Full Scan' | 'Passive Scan'")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
