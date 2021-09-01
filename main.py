import discord
import os
import requests
import json
from keep_alive import keep_alive


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

@client.event
async def on__raw_reaction_add(payload):
  payload_message_id = payload.message_id
  target_message_id = 882497078876602368

  if payload_message_id == target_message_id:
    print(payload.emoji.name)
    if payload.emoji.name == ":sunglasses:":
      print("reacted with sunglasses")
    # to give that person a role


keep_alive()
client.run(os.getenv('TOKEN'))