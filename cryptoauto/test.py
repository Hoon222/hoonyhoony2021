import pyupbit

access = "W1GrhxCCTYfLblVTNcXWzZKEpKh8XB8LOfYt6xsy"          # 본인 값으로 변경
secret = "f9L0nYI73rlUtwrS6hbzVc00BCHx1TaA7CtG9l0g"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회