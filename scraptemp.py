#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, re, os
from datetime import datetime

HEADERS = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36',
}

class ScrapTemp(object):
    """Scrap LN Home
        la página del servicio meteorologico(http://www.smn.gov.ar/?mod=prensa&id=200) desde ajax consulta self.url_bsas_temp

        pendiente: escrapear self.output_path
    
    """
    BASE = os.path.dirname(os.path.abspath(__file__))
    
    template = "\"\nTemperature: {temp}\nFeels Like: {fell}\nHumidity: {hum}%\n\""
    
    url_table_temp = "http://www.smn.gov.ar/?mod=dpd&id=21&e=total"
    url_bsas_temp = "http://www.smn.gov.ar/layouts/temperatura_layout.php?d=0.7334670192534647"
    
    output_path = os.path.join(os.path.join(BASE, "."), "data")
    output_file = os.path.join(output_path, "bsas_temp.txt")
    last_modified = os.path.join(output_path, "last_modified.txt")


    def __init__(self):
        super(ScrapTemp, self).__init__()
        # print "scraping ..."

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


        self.get_bsas_temp()

    
    def get_bsas_temp(self):

        r = requests.get(self.url_bsas_temp, headers=HEADERS)
        r.encoding = 'utf-8'
        
        temp = r.text.split("\n")[0]
        regex = re.compile(r".C.+", re.IGNORECASE)
        
        temp = regex.sub("", temp)
        output =  self.template.format(temp=temp, fell=0, hum=0)

        text_file = open(self.output_file, "w")
        text_file.write(output)
        text_file.close()

        # logging last_modified...
        text_file = open(self.last_modified, "w")
        text_file.write(str(datetime.now()))
        text_file.close()
        
        # return temp




ScrapTemp()
