import logging
import psycopg2
import os
import pandas as pd

import helpers.utils as utils


class Connection(object):
    """Generic reader of database connection"""
    def run(self, query, outfilename, queryparams=None, debug=False):
        logger = logging.getLogger(__name__)
        hydratedquery = self.hydrate(query, queryparams)

        if debug:
            logger.debug(hydratedquery)
            with open('query.sql', 'w') as f:
                f.write(hydratedquery)

        if not os.path.exists(outfilename):
            logger.info("Reading against the database")
            df = self.run_sql(hydratedquery)
            df.to_csv(outfilename, encoding='utf-8', index=False)
        else:
            logger.info("Cache file exists, using that")
            df = pd.read_csv(outfilename, encoding='utf-8')

        return df

    def hydrate(self, query, queryparams=None):
        """A lot of the queries we seem to have involve queryparams."""
        if queryparams is None:
            queryparams = dict()
        return query.format(**queryparams)


class RedShiftConnection(Connection):
    """Connects to redshift, provides methods for running"""
    def __init__(self, credentials):
        super(RedShiftConnection, self).__init__()
        self.credentials = credentials
        self.connect()

    def connect(self):
        """Connect to redshift."""
        try:
            self.connection = psycopg2.connect(
                database=self.credentials['database'],
                host=self.credentials['host'],
                port=self.credentials['port'],
                user=self.credentials['username'],
                password=self.credentials['password']
            )
        except:
            print('Unable to connect to database {}'.format(self.credentials['database']))

    def run_sql(self, query_file):
        """Gets the data from redshift."""
        df = pd.read_sql(query_file, self.connection)
        return df

    def query(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        return cur.fetchall()
