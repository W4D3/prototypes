from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class EligibilityCheck(Form):
    """
    Simple login class to capture the required fields for an eligibility chck
    """
    # Required fields from the human
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    member_id = StringField('member_id', validators=[DataRequired()])
    birth_date = StringField('birth_date', validators=[DataRequired()])
    # required fields from the doctor
    npi = StringField('npi', validators=[DataRequired()])
    dr_first_name = StringField('dr_first_name', validators=[DataRequired()])
    dr_last_name = StringField('dr_last_name', validators=[DataRequired()])
