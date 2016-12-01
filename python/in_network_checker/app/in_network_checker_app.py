from app import app
from app import pd
import json
from .forms import LoginForm
from flask import render_template

# index view function suppressed for brevity
# set up the route for the simple form
@app.route('/in_network_checker', methods=['GET', 'POST'])
def driver():
    # make a simple form
    form = LoginForm()
    # the value of this parameter is inherited from: flask.ext.wtf.Form
    if form.validate_on_submit():
        # get all of the data from your LoginForm
        params = {
            "birth_date": form.birth_date.data,
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "member_id": form.member_id.data,
            "dr_first_name": form.dr_first_name.data,
            "dr_last_name": form.dr_last_name.data,
            "npi": form.npi.data,
        }
        # get and return the response of the eligibility check
        response = eligibility(params)
        return response
    return render_template('in_network_checker.html',
                           title='Cigna-In Network Checker',
                           form=form)

# simple home page
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'DKG'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.route('/index/eligibility')
def eligibility(params):
    # properly format the input parameters into a PokitDok Eligibility Call
    # documentation: https://platform.pokitdok.com/documentation/v4/#eligibility
    eligibility_check = pd.eligibility({
        "member": {
            "birth_date": params["birth_date"],
            "first_name": params["first_name"],
            "last_name": params["last_name"],
            "id": params["member_id"]
        },
        "provider": {
            "first_name": params["dr_first_name"],
            "last_name": params["dr_last_name"],
            "npi": params["npi"]
        },
        "trading_partner_id": "cigna"
    })
    try:
        # from Cigna, the information about in-network is available at this level of the response
        return_payload = eligibility_check["data"]["coverage"]["messages"]
    except Exception:
        # if it fails, produce the whole eligibility response for debugging
        return_payload = eligibility_check
        pass
    return json.dumps(return_payload)