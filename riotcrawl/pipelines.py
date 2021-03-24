''' Pipelines to process scraped Data

Attributes
----------
DIR : str 
    The directory to which files should
    be written.
TIMESTAMP : :obj: datetime 
    The current date and time;
    formatted.
FILE : str
    The name of the File to write.
'''
import os
from pathlib import Path
from datetime import datetime
from scrapy.exporters import JsonLinesItemExporter

HOME = str(Path.home())
FOLDER = 'Riotz/'

PATH = os.path.join(HOME, FOLDER)
TIMESTAMP = datetime.now().strftime("%Y%m%d")
FILE = f'{PATH}{TIMESTAMP}.json'

# Check if Path exists
# If not, one will be
# created.
#
if not os.path.exists(PATH):
    os.mkdir(PATH)

class RiotcrawlPipeline:
    ''' Pipeline of chronik_blackblogs

    Process Data and save them in
    a json file.

    Attributes
    ----------
    posts_file : func
        Opens the file with the Data.
    exporter : scrapy exporter
        Exports the Data to a JSON
        format.
    exporter : func
        Start the process of export.
    '''
    def __init__(self):
        self.posts_file = open(FILE, 'wb')
        # The Second Argument in self.exporter
        # is the protocol used by pickle;
        # If the Python version <= 3.8 ,
        # use 4 or less.
        self.exporter = JsonLinesItemExporter(
                self.posts_file,
                encoding = 'utf-8',
                ensure_ascii = False,
                )
        self.exporter.start_exporting()

    def close_spider(self, spider):
        ''' Finish Supporter and Close File
        
        Parameters 
        ----------
        spider : :obj: spider
            Stop Process for given Spider.
        '''
        self.exporter.finish_exporting()
        self.posts_file.close()

    def process_item(self, item, spider):
        ''' Export Scraped Items

        Parameters
        ----------
        item : scrapy :obj: Item
            The scraped Items to process.
        spider : scrapy :obj: spider
            The Spider the item is recieved
            from.
        '''
        self.exporter.export_item(item)
        return item



