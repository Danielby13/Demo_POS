import qrcode
from PIL import Image
import json
import datetime


def items_data_import(invoice, temp): # Arrange the data to match the way the database gets
    items_details_dict = {}
    i = 1
    for item in temp:
        index = "item{0}".format(i)
        items_details_dict[index] = {}
        items_details_dict[index] = item
        i = i + 1
    invoice['details'] = str(items_details_dict).replace("'", '"')
    my_string = '"approved_status": {0},"category": "{1}", "credit_number": {2}, "customer_email": "{3}",' \
                '"customer_id": "{4}", "customer_phone_number": "{5}", "details": {6},' \
                ' "invoice_number": "{7}", "payment_type": "{8}", "payments": {9}, ' \
                ' "refund": {10}, "seller_name": "{11}", "store_address": "{12}", "store_city": "{13}",' \
                ' "store_id": "{14}", "store_name": "{15}","store_phone": {16}, "total_amount": {17},' \
                ' "transaction_date": "{18}", "vat": {19}, "warranty": {20} '.format(invoice['approved_status'], invoice['category'], invoice['credit_number'], invoice['customer_email'], invoice['customer_id'], invoice['customer_phone_number'], invoice['details'], invoice['invoice_number'], invoice['payment_type'], invoice['payments'], invoice['refund'], invoice['seller_name'], invoice['store_address'], invoice['store_city'], invoice['store_id'], invoice['store_name'], invoice['store_phone'], invoice['total_amount'], "empty6", invoice['vat'], invoice['warranty'])
    return my_string


def qr_generator(invoice, temp): # Generate QR code with the data from "items_data_import" function
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        ) # initilize empty QR code
        temp = "[{"+items_data_import(invoice, temp)+"}]"
        qr.add_data(temp) # insert data to the QR code

        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img.save("output.png") # save the QR code 
    except Exception as e:
        print(e)

