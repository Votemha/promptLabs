from gigachat import GigaChat

with GigaChat(credentials="OThhZGViNTgtN2E0Mi00YmExLTgzMTctM2YwNjFmNGI0NzNkOmM2YzYzMGJlLTczMGQtNDk3MC04MjRlLWQwZjBkZWRkM2U5Mg==",
              ca_bundle_file="/Users/artemahmetov/Downloads/russiantrustedca/russiantrustedca.pem",
              model='Gigachat-2-Pro',
              scope='GIGACHAT_API_B2B') as giga:
   response = giga.chat("Привет! Объясни, что такое искусственный интеллект простыми словами.")
   print(response.choices[0].message.content)

print(response)