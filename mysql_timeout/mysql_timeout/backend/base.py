import logging

from django.db.backends.mysql.base import DatabaseWrapper as MysqlDatabaseWrapper

logger = logging.getLogger('main')


class DatabaseWrapper(MysqlDatabaseWrapper):

    def close_if_unusable_or_obsolete(self):
        super(DatabaseWrapper, self).close_if_unusable_or_obsolete()
        logger.info('close_if_unusable_or_obsolete')

    def connect(self):
        super(DatabaseWrapper, self).connect()
        logger.info('new connect')
        logger.info(self.close_at)

    def close(self):
        logger.info('close connection')
        super(DatabaseWrapper, self).close()
