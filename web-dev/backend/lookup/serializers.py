from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import *


class Quarterly_Real_GDP_Serializer(ModelSerializer):
    class Meta:
        model = Quarterly_Real_GDP
        fields = '__all__'

class Annual_Real_GDP_Serializer(ModelSerializer):
    class Meta:
        model = Annual_Real_GDP
        fields = '__all__'

class Real_GDP_Per_Capita_Serializer(ModelSerializer):
    class Meta:
        model = Real_GDP_Per_Capita
        fields = '__all__'

class Daily_3month_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Daily_3month_Treasury_Yield
        fields = '__all__'

class Weekly_3month_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_3month_Treasury_Yield
        fields = '__all__'

class Monthly_3month_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_3month_Treasury_Yield
        fields = '__all__'

class Daily_2year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Daily_2year_Treasury_Yield
        fields = '__all__'

class Weekly_2year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_2year_Treasury_Yield
        fields = '__all__'

class Monthly_2year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_2year_Treasury_Yield
        fields = '__all__'

class Daily_5year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Daily_5year_Treasury_Yield
        fields = '__all__'

class Weekly_5year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_5year_Treasury_Yield
        fields = '__all__'

class Monthly_5year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_5year_Treasury_Yield
        fields = '__all__'

class Daily_7year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Daily_7year_Treasury_Yield
        fields = '__all__'

class Weekly_7year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_7year_Treasury_Yield
        fields = '__all__'

class Monthly_7year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_7year_Treasury_Yield
        fields = '__all__'

class Daily_10year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Daily_10year_Treasury_Yield
        fields = '__all__'

class Weekly_10year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_10year_Treasury_Yield
        fields = '__all__'

class Monthly_10year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_10year_Treasury_Yield
        fields = '__all__'
 
class Daily_30year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Daily_30year_Treasury_Yield
        fields = '__all__'

class Weekly_30year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_30year_Treasury_Yield
        fields = '__all__'

class Monthly_30year_Treasury_Yield_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_30year_Treasury_Yield
        fields = '__all__'

class Daily_Federal_Funds_Rate_Serializer(ModelSerializer):
    class Meta:
        model = Daily_Federal_Funds_Rate
        fields = '__all__'

class Weekly_Federal_Funds_Rate_Serializer(ModelSerializer):
    class Meta:
        model = Weekly_Federal_Funds_Rate
        fields = '__all__'

class Monthly_Federal_Funds_Rate_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_Federal_Funds_Rate
        fields = '__all__'

class Monthly_Cpi_Serializer(ModelSerializer):
    class Meta:
        model = Monthly_Cpi
        fields = '__all__'

class Semiannual_Cpi_Serializer(ModelSerializer):
    class Meta:
        model = Semiannual_Cpi
        fields = '__all__'

class Inflation_Serializer(ModelSerializer):
    class Meta:
        model = Inflation
        fields = '__all__'

class Inflation_Expectation_Serializer(ModelSerializer):
    class Meta:
        model = Inflation_Expectation
        fields = '__all__'

class Consumer_Sentiment_Serializer(ModelSerializer):
    class Meta:
        model = Consumer_Sentiment
        fields = '__all__'

class Retail_Sales_Serializer(ModelSerializer):
    class Meta:
        model = Retail_Sales
        fields = '__all__'

class Durables_Serializer(ModelSerializer):
    class Meta:
        model = Durables
        fields = '__all__'

class Unemployment_Serializer(ModelSerializer):
    class Meta:
        model = Unemployment
        fields = '__all__'

class Nonfarm_Payroll_Serializer(ModelSerializer):
    class Meta:
        model = Nonfarm_Payroll
        fields = '__all__'

class Annual_Income_Statement_Serializer(ModelSerializer):
    class Meta:
        model = Annual_Income_Statement
        fields = '__all__'

class Quarterly_Income_Statement_Serializer(ModelSerializer):
    class Meta:
        model = Quarterly_Income_Statement
        fields = '__all__'

class Annual_Balance_Sheet_Serializer(ModelSerializer):
    class Meta:
        model = Annual_Balance_Sheet
        fields = '__all__'

class Quarterly_Balance_Sheet_Serializer(ModelSerializer):
    class Meta:
        model = Quarterly_Balance_Sheet
        fields = '__all__'

class Annual_Cash_Flow_Serializer(ModelSerializer):
    class Meta:
        model = Annual_Cash_Flow
        fields = '__all__'

class Quarterly_Cash_Flow_Serializer(ModelSerializer):
    class Meta:
        model = Quarterly_Cash_Flow
        fields = '__all__'

class Earning_Serializer(ModelSerializer):
    class Meta:
        model = Earning
        fields = '__all__'

class Overview_Serializer(ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'

class Earning_Calendar_Serializer(ModelSerializer):
    class Meta:
        model = Earning_Calendar
        fields = '__all__'