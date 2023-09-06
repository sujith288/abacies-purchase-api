from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.views import APIView
import pandas as pd


@api_view(['POST'])
def RefillProductView(self,request, pk,format=None):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        response_data = {"error": "No product is found with that product id"}
        return "error"
    
    quantity = request.data.get("quantity", None)
    if quantity<=0:
        response_data = {"error": "Please enter a quantity greater than 0"}
        return Response(response_data)
    if quantity:
        Refill.objects.create(
            product=product,
            quantity=quantity
        )
        product.quantity+=quantity
        product.save()
        response_data = {"success": "Product has been successfully updated"}
        return Response(response_data)
   

@api_view(['POST'])
def AddNewProductView(self,request,format=None):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        data = serializer.errors
        return Response(data)
    

'''
View Where we save the purchases report and update the available stock of product 
based on the quantity of product purchased
'''
class PurchaseView(APIView):
    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            product_ids = {d["product_id"]: d["quantity"] for d in request.data }       
            products = Product.objects.filter(id__in=product_ids.keys())
            update_products = []
            for product in products:
                product.quantity -= product_ids[product.id] #decrementing the available stock from the available_stock here
                update_products.append(product)
            if update_products:
                Product.objects.bulk_update(update_products, ['available_product_stock'])
                return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ExportPurchaseCsv(APIView):
    def get(self,request):
        print("hello")
        purchase_objs = Purchase.objects.filter(csv_exported=False).all() #filter query
        if purchase_objs:
            serializer = PurchaseSerializertest(purchase_objs,many=True)
            df = pd.DataFrame(serializer.data)
            df.to_csv(f"./purchase_export/{uuid.uuid4()}.csv", encoding="UTF-8", index=False)
            purchase_objs.update(csv_exported=True)
            return Response({'status': 200})
        else:
            response_data = {"error": "No data to export"}
            return Response(response_data) 







