# -*- coding: utf-8 -*-
from pushover import Client
 
client = Client("uaP3kPqNsnccmJhjvwRzGK3Hbsh1K5", api_token="aaFWwMm1G3YP2iPKNPjTsHa3QEc6tS")
client.send_message("Test Mesaji", title="Test Basligi")
client.send_message("Deneme Mesajı", title="DENEME BAŞLIĞIS")