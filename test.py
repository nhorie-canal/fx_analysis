import oandapy

access_token = "09ed0a97daac0bc3be11428eb4f0b18b-01b9c01054551d9aa570713307ab7f1a"

oanda = oandapy.API(environment="practice", access_token=access_token)

res = oanda.get_history(instrument="USD_JPY",granularity="H1",count=2)
print(res)