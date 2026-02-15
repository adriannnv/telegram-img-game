import asyncio
import qrcode
import os
from dotenv import load_dotenv
from telethon import TelegramClient, errors

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = "my_session"

async def main():
	client = TelegramClient(session_name, api_id, api_hash)
	print("Connecting\n")
	await client.connect()

	if await client.is_user_authorized():
		me = await client.get_me()
		print("Already logged in as", me.username)
		return
	
	print("Requesting QR\n")
	qr_login = await client.qr_login()

	while True:
		print("Scan this QR Code:\n")
		qr = qrcode.QRCode()
		qr.add_data(qr_login.url)
		qr.make()
		qr.print_ascii(invert=True)


		try:
			user = await qr_login.wait(timeout=60)
			print("Login succesful: ", user.username)
		except asyncio.TimeoutError:
			print("QR expired, regenerating..")
			await qr_login.recreate()

asyncio.run(main())
