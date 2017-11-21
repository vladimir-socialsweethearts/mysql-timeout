from django.db.backends.mysql.base import DatabaseWrapper as MysqlDatabaseWrapper


class DatabaseWrapper(MysqlDatabaseWrapper):

    def close_if_unusable_or_obsolete(self):
        super(DatabaseWrapper, self).close_if_unusable_or_obsolete()
        print('close_if_unusable_or_obsolete')

    def connect(self):
        super(DatabaseWrapper, self).connect()
        print('new connect')
        print(self.close_at)

    def close(self):
        print('close connection')
        super(DatabaseWrapper, self).close()
