import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from read_properties import properties
from resources.scrape import WebsiteScrape
from resources.rag import WebsiteRag
from resources.web_ops import RetrieveDistinctData, deleteRecords



app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(WebsiteScrape, '/wb/website_scrape')
api.add_resource(WebsiteRag, '/wb/website_rag')
api.add_resource(RetrieveDistinctData, '/wb/retrieve_distinct_data')
api.add_resource(deleteRecords, '/wb/delete_records')




if __name__ == "__main__":
    log_file_format = ('%(levelname)s - [%(asctime)s] - p%(process)s - {%(filename)s: %(funcName)s :%(lineno)d} -> %('
                       'message)s')
    logging.basicConfig(filename=properties["log_file_name"], format=log_file_format, level=logging.INFO)
    app.run(host=properties["host_name"], port=int(properties["port"]))
