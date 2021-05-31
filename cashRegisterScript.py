import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import store_data, qrGen
import random

# Initialize firestore database
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # connect to db
collection = db.collection('users')


class Invoice(object):
    def __init__(self, data_store, total_amount, getUid, userData, items_details_dict): 
        self.approved_status = 0
        self.category = data_store['store_details']['category']
        self.credit_number = 0 if data_store['purchase_details']['credit_number'] == "" else data_store['purchase_details']['credit_number']
        self.customer_email = userData['email']
        self.customer_id = getUid
        self.customer_phone_number = userData['phoneNumber']
        self.details = items_details_dict
        self.invoice_number = random_number_gen()
        self.payment_type = data_store['purchase_details']['payment_type']
        self.payments = 0 if data_store['purchase_details']['payment_type'] == "מזומן" else data_store['purchase_details']['payments']
        self.refund = 0
        self.seller_name = data_store['store_details']['seller_name']
        self.store_address = data_store['store_details']['store_address']
        self.store_city = data_store['store_details']['store_city']
        self.store_name = data_store['store_details']['store_name']
        self.store_phone = data_store['store_details']['store_phone']
        self.store_id = data_store['store_details']['store_id']
        self.total_amount = total_amount
        self.transaction_date = datetime.datetime.now()
        self.vat = data_store['purchase_details']['vat']
        self.warranty = data_store['purchase_details']['warranty']

    def to_dict(self): # transfer the data to dict 
        dest = {
            u"approved_status": self.approved_status,
            u"category": self.category,
            u"credit_number": self.credit_number,
            u"customer_email": self.customer_email,
            u"customer_id": self.customer_id,
            u"customer_phone_number": self.customer_phone_number,
            u"details": self.details,
            u"invoice_number": self.invoice_number,
            u"payment_type": self.payment_type,
            u"payments": self.payments,
            u"refund": self.refund,
            u"seller_name": self.seller_name,
            u"store_address": self.store_address,
            u"store_city": self.store_city,
            u"store_id": self.store_id,
            u"store_name": self.store_name,
            u"store_phone": self.store_phone,
            u"total_amount": self.total_amount,
            u"transaction_date": self.transaction_date,
            u"vat": self.vat,
            u"warranty": self.warranty,
        }
        return dest


def random_number_gen(): # generate random number for invoice id
    return random.randint(1000, 1000000000)


def getUserData(phone):
    try:
        doc = collection.where(u'phoneNumber', u'==', phone)  # find the user
        res = doc.get()
        getUid = ''
        userData = {}
        for doc in res:
            getUid = doc.id
            userData = doc.to_dict()
        return {'userData': userData, 'getUID': getUid}
    except:
        print("User does not exist")


def setInvoiceDataToDB(phone, data_store, total_amount, items_details_dict): # send data to the DB
    res = getUserData(phone)
    if res['getUID'] != '':
        invoice = Invoice(data_store=data_store, total_amount=total_amount, getUid=res['getUID'], userData=res['userData'], items_details_dict=items_details_dict)
        db.collection(u'invoices').add(invoice.to_dict())
    else:
        print("User does not exist")


def setInvoiceDataToDb_QR(data_store, total_amount, items_details_dict, temp): # send data to generate QR code
    res = {"userData": {"firstName": "empty1", "email": "empty2", "lastName": "empty3", "phoneNumber": "empty4", "active": "1"}, "getUID": "empty5"}
    invoice = Invoice(data_store=data_store, total_amount=total_amount, getUid=res["getUID"], userData=res["userData"],items_details_dict=items_details_dict)
    qrGen.qr_generator(invoice.to_dict(), temp)
