from django.shortcuts import render, get_object_or_404, redirect
from WebShopiApp.models import Cart
from forex_python.converter import CurrencyRates
import math
import qrcode

def payment_gateway(request):
    upi_id = 'sandipyadav90840-1@okicic'

    cart = get_object_or_404(Cart, user=request.user)
    items = cart.cart_items.all()

    # subtotal in USD
    subtotal = sum(item.total_price() for item in items)

    # convert to INR
    currency_rate = CurrencyRates()
    change_rate = currency_rate.get_rate('USD', 'INR')
    subtotal_in_inr = float(subtotal) * change_rate

    # GST 18%
    gst = subtotal_in_inr * 0.18
    total_in_inr = subtotal_in_inr + gst

    # rounding to 2 decimals
    subtotal_in_inr = round(subtotal_in_inr, 2)
    gst = round(gst, 2)
    final_value = round(total_in_inr, 2)

    request.session['final_value'] = final_value
    # request.session.modified = True 


    qr_data = f"upi://pay?pa={upi_id}&pn={request.user.username}&am={final_value}&tn=Payment for {final_value}"
    payment_qr_code = qrcode.make(qr_data)
    payment_qr_code.save("QR.png")

    context = {
        'items': items,
        'subtotal': subtotal_in_inr,
        'gst': gst,
        'final_value': final_value,
        'upi_id': upi_id,
    }
    return render(request, "paypage.html", context)


def paypage(request):
    final_value = request.session.get('final_value')
    print("Final value from session:", final_value)  
    if final_value is None:
        return redirect('payment_gateway')  

    return render(request, 'paygateway.html', {'final_value': final_value})
