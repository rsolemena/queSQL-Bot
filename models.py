from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(255))
    flat_no = db.Column(db.String(255))
    floor = db.Column(db.String(255))
    street = db.Column(db.String(255))
    street_no = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))
    live_time = db.Column(db.String(255))
    flat_floor = db.Column(db.String(255))
    previous_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    full_address = db.Column(db.String(255))
    neighborhood = db.Column(db.String(255))
    state = db.Column(db.String(255))
    municipality = db.Column(db.String(255))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni = db.Column(db.String(255), nullable=False, unique=True)
    advertising_accepted = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(255))
    personal_details_id = db.Column(db.Integer)
    contact_details_id = db.Column(db.Integer)
    debit_card_id = db.Column(db.Integer)
    bank_account_id = db.Column(db.Integer)
    employment_details_id = db.Column(db.Integer)
    address_id = db.Column(db.Integer)
    password = db.Column(db.String(255))
    password_change_key = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    campaign = db.Column(db.String(255))
    id_result = db.Column(db.String(255))
    dni_expiration_date = db.Column(db.String(255))
    dni_office_code = db.Column(db.String(255))
    sent_to_badexcug = db.Column(db.Boolean, default=False)
    requested_fields = db.Column(db.Text)
    more_info_requested_time = db.Column(db.DateTime)
    more_info_provided_time = db.Column(db.DateTime)
    password_expiration_date = db.Column(db.Date)
    bo_cre_blocked_at = db.Column(db.DateTime)
    la_ref = db.Column(db.String(255))
    la_uri = db.Column(db.String(255))
    last_login = db.Column(db.DateTime)
    flow_name = db.Column(db.String(255))
    l_max_amount = db.Column(db.Integer)
    l_interest = db.Column(db.Numeric(5, 4))
    deleted_at = db.Column(db.Date)
    promo_code_id = db.Column(db.Integer)
    fraud_at = db.Column(db.Date)
    public_id = db.Column(db.String(255), unique=True)
    application_screening_processed_at = db.Column(db.DateTime)
    customer_onboarding_processed_at = db.Column(db.Date)
    onboarding_processed_at = db.Column(db.DateTime)
    password_change_expired_at = db.Column(db.DateTime)
    id_check_status = db.Column(db.String(255))
    data_treatment_accepted = db.Column(db.Boolean, default=False)
    loyalty_details_id = db.Column(db.BigInteger, db.ForeignKey('loyalty_details.id'))
    uid = db.Column(db.String(255))
    dni_right_part = db.Column(db.String(9))
    last_otp_at = db.Column(db.DateTime)

class Promise(db.Model):
    __tablename__ = 'promises'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    due_date = db.Column(db.Date)
    amount = db.Column(db.Float)
    forgiven_amount = db.Column(db.Float)
    status = db.Column(db.String(255))
    loan_application_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    is_partial = db.Column(db.Boolean)
    forgiven = db.Column(db.Boolean, default=False)
    back_office_user_id = db.Column(db.Integer)
    source = db.Column(db.String(255))

class PersonalDetail(db.Model):
    __tablename__ = 'personal_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dependants = db.Column(db.Integer)
    dob = db.Column(db.Date)
    educational_level = db.Column(db.String(255))
    home_status = db.Column(db.String(255))
    marital_status = db.Column(db.String(255))
    monthly_home_income = db.Column(db.Numeric(10, 0))
    max_amount_research = db.Column(db.Numeric(19, 2))
    owns_driving_license = db.Column(db.Boolean)
    license_start_date = db.Column(db.Date)
    gender = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    compound_name = db.Column(db.String(255))
    nationality = db.Column(db.String(255))
    enriched_compound_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birth_country = db.Column(db.String(255))
    federal_entity = db.Column(db.String(255))

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float)
    loan_application_id = db.Column(db.Integer)
    status = db.Column(db.String(255))
    requested_by = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    paid_at = db.Column(db.Date)
    amort_capital = db.Column(db.Float)
    amort_comissions = db.Column(db.Float)
    amort_del_comissions = db.Column(db.Float)
    paid_acc = db.Column(db.String(255))
    paid_bank = db.Column(db.String(255))
    recovery_agent = db.Column(db.String(255))
    payment_type = db.Column(db.String(255))
    debit_card_id = db.Column(db.Integer)
    charge_id = db.Column(db.String(255))
    aml_processed_at = db.Column(db.DateTime)
    point_of_sale_merchant_id = db.Column(db.String(255))
    spreedly_transaction_token = db.Column(db.String(255), unique=True)
    is_3ds = db.Column(db.Boolean)
    version_of_3ds = db.Column(db.Integer)
    checkout_payment_id = db.Column(db.String(255))
    payment_method = db.Column(db.String(255))
    payment_channel = db.Column(db.String(255))
    recovery_campaign_id = db.Column(db.BigInteger)
    payment_link = db.Column(db.Boolean)
    recovery_offer_id = db.Column(db.BigInteger)
    refunded_id = db.Column(db.Integer)
    openpay_payment_id = db.Column(db.String(255))
    payment_plan_id = db.Column(db.Integer)
    conekta_payment_id = db.Column(db.String(255))
    nuvei_payment_id = db.Column(db.String(255))

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    loan_application_id = db.Column(db.Integer, db.ForeignKey('loan_applications.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ref_id = db.Column(db.String(255))
    status = db.Column(db.String(255))
    status_history = db.Column(db.String(255))
    early_payments = db.Column(db.Text)
    amount = db.Column(db.Float)
    days = db.Column(db.Integer)
    promo_code_id = db.Column(db.Integer)
    rate = db.Column(db.Float)
    interests = db.Column(db.Float)
    total_to_pay = db.Column(db.Float)
    remaining_to_pay = db.Column(db.Float)
    due_date = db.Column(db.Date)
    transfer_date = db.Column(db.DateTime)
    transfer_origin_account = db.Column(db.String(255))
    pay_with = db.Column(db.String(255))
    three_days_alert_sent_email = db.Column(db.Boolean)
    one_day_alert_sent_email = db.Column(db.Boolean)
    one_day_alert_sent_sms = db.Column(db.Boolean)
    choices = db.Column(db.Text)
    paid_on_date = db.Column(db.Boolean)
    paying = db.Column(db.Boolean)
    recovery_agency = db.Column(db.String(255))
    payment_plan_allowed = db.Column(db.Boolean)
    close_date = db.Column(db.Date)
    aml_processed_at = db.Column(db.DateTime)
    aml_application_screening_processed_at = db.Column(db.DateTime)
    harvest_discount_in_percentage = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    loan_number = db.Column(db.Integer)
    loyalty_level_id = db.Column(db.BigInteger)

class LoanApplication(db.Model):
    __tablename__ = 'loan_applications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(255))
    ref_id = db.Column(db.String(255), unique=True)
    payment_method = db.Column(db.String(255))
    usage = db.Column(db.String(255))
    early_payments = db.Column(db.Text)
    amount = db.Column(db.Float, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    fee = db.Column(db.Float)
    rate = db.Column(db.Float)
    interests = db.Column(db.Float)
    total_to_pay = db.Column(db.Float)
    remaining_to_pay = db.Column(db.Float)
    due_date = db.Column(db.Date)
    expected_transfer_date = db.Column(db.DateTime)
    transfer_date = db.Column(db.DateTime)
    three_days_alert_sent_email = db.Column(db.Boolean, default=False)
    one_day_alert_sent_email = db.Column(db.Boolean, default=False)
    one_day_alert_sent_sms = db.Column(db.Boolean, default=False)
    paid_on_date = db.Column(db.Boolean)
    ip_address = db.Column(db.String(255))
    personal_details_id = db.Column(db.Integer)
    contact_details_id = db.Column(db.Integer)
    debit_card_id = db.Column(db.Integer)
    bank_account_id = db.Column(db.Integer)
    employment_details_id = db.Column(db.Integer)
    address_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    geo_ip_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    prev_status = db.Column(db.String(255))
    cre2_decision = db.Column(db.String(255))
    bank_data_status = db.Column(db.String(255))
    transfer_origin = db.Column(db.String(255))
    transfer_type = db.Column(db.String(255))
    transfer_fetched = db.Column(db.Boolean, default=False)
    fingerprint = db.Column(db.String(255))
    cookie = db.Column(db.String(255))
    paying = db.Column(db.Boolean, default=False)
    requested_fields = db.Column(db.Text)
    requested_fields_time = db.Column(db.DateTime)
    user_agent = db.Column(db.String(255))
    pay_with = db.Column(db.String(255))
    recovery_agent = db.Column(db.String(255))
    pplan_allowed = db.Column(db.Boolean, default=False)
    next_working_day = db.Column(db.Boolean, default=False)
    choices = db.Column(db.Text)
    is_returning = db.Column(db.Boolean, default=False)
    has_completed_form = db.Column(db.Boolean, default=False)
    first_time_cre = db.Column(db.Boolean, default=False)
    has_been_in_error_cre_queue = db.Column(db.DateTime)
    deenero_bank_account = db.Column(db.String(255))
    sent_to_recovery = db.Column(db.DateTime)
    return_from_recovery = db.Column(db.DateTime)
    first_app = db.Column(db.Boolean, default=False)
    l_max_amount = db.Column(db.Integer)
    new_terms_reason = db.Column(db.String(255))
    prev_amount = db.Column(db.Float)
    close_date = db.Column(db.Date)
    flow_name = db.Column(db.String(255))
    application_step = db.Column(db.String(255))
    promo_code_id = db.Column(db.Integer)
    application_path = db.Column(db.String(255))
    app_name = db.Column(db.String(255))
    aml_processed_at = db.Column(db.DateTime)
    transfer_request_sent = db.Column(db.Boolean, default=False)
    force_transfer_through_robots = db.Column(db.Boolean, default=False)
    aml_application_screening_processed_at = db.Column(db.DateTime)
    dni_uploaded_conversion_front = db.Column(db.Boolean, default=False)
    dni_uploaded_conversion_back = db.Column(db.Boolean, default=False)
    preferred_payback_method = db.Column(db.String(255), default='debit_card')
    harvest_discount_in_percentage = db.Column(db.Integer)
    custom_flow = db.Column(db.String(255))
    control_group = db.Column(db.Boolean)
    application_attempt = db.Column(db.Integer)
    evaluation_model_name = db.Column(db.String(255))
    income_source = db.Column(db.String(255))
    is_assisted = db.Column(db.Boolean, default=False)
    block_postbacks = db.Column(db.Boolean, default=False)
