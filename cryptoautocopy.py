import time
import pyupbit
import datetime

access = "xhySnaRtv3EYW6QC3b7Zwo888a5cc8h0SXqUTE7M"
secret = "8gxbf9Ra5GhbFS86JWnXSYHmxm0rg3xrgyIwprWi"


def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# BTC 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=300):  # 8:55분 ~ 9:00 까지 출금 시간
            target_price = get_target_price("KRW-BTC", 0.1)     # 티커, K값(기본 0.5)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.1995)   # 잔고 = 1, 1/거래 코인 수 - fee
        else:
            btc = get_balance("BTC")
            if btc > 0.00000001:       # 약 5000원 이상으로 맞춤(현재는 최저로 맞춤. 추후 판매 오류로 프로그램 다운 시 수정)
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

# XRP 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-XRP")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=300):  # 8:55분 ~ 9:00 까지 출금 시간
            target_price = get_target_price("KRW-XRP", 0.1)     # 티커, K값
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XRP", krw*0.1995)   # 잔고 = 1, 1/거래 코인 수 - fee
        else:
            btc = get_balance("XRP")
            if btc > 0.00000001:       # 약 5000원 이상으로 맞춤(현재는 최저로 맞춤. 추후 판매 오류로 프로그램 다운 시 수정)
                upbit.sell_market_order("KRW-XRP", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)


# ETH 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=300):  # 8:55분 ~ 9:00 까지 출금 시간
            target_price = get_target_price("KRW-ETH", 0.1)     # 티커, K값
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.1995)   # 잔고 = 1, 1/거래 코인 수 - fee
        else:
            btc = get_balance("ETH")
            if btc > 0.00000001:       # 약 5000원 이상으로 맞춤(현재는 최저로 맞춤. 추후 판매 오류로 프로그램 다운 시 수정)
                upbit.sell_market_order("KRW-ETH", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)


# BTT 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTT")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=300):  # 8:55분 ~ 9:00 까지 출금 시간
            target_price = get_target_price("KRW-BTT", 0.3)     # 티커, K값
            current_price = get_current_price("KRW-BTT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTT", krw*0.1995)   # 잔고 = 1, 1/거래 코인 수 - fee
        else:
            btc = get_balance("BTT")
            if btc > 0.00000001:       # 약 5000원 이상으로 맞춤(현재는 최저로 맞춤. 추후 판매 오류로 프로그램 다운 시 수정)
                upbit.sell_market_order("KRW-BTT", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)


# NEO 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-NEO")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=300):  # 8:55분 ~ 9:00 까지 출금 시간
            target_price = get_target_price("KRW-NEO", 0.1)     # 티커, K값
            current_price = get_current_price("KRW-NEO")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-NEO", krw*0.1995)   # 잔고 = 1, 1/거래 코인 수 - fee
        else:
            btc = get_balance("NEO")
            if btc > 0.00000001:       # 약 5000원 이상으로 맞춤(현재는 최저로 맞춤. 추후 판매 오류로 프로그램 다운 시 수정)
                upbit.sell_market_order("KRW-NEO", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
