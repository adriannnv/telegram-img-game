# telethon - Notes

## What is it?
`telethon` is a library that interacts with telegram's API.
Telegram uses its own solution to sending messages, MTProto, a protocol which sends binary data through a tcp-like conection.
Different to tcp's implementation, once you send a message, the connection remains open, skipping the reconnection step.
You can connect to a telegram account as either a bot or a real person.