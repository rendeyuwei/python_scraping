from pymongo import MongoClient


class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = MongoClient(host=self.db_ip, port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[table_name]

    def get_one(self, query):
        # 获取一个指定的值，并且将_id字段不返回
        return self.table.find_one(query, projection={"_id": False})

    # 获取数据库满足条件的所有数据
    def get_all(self, query):
        return self.table.find(query)

    # 向集合中添加数据
    def add(self, kv_dict):
        return self.table.insert(kv_dict)

    # 删除集合中的数据
    def delete(self, query):
        return self.table.delete_many(query)

    # 查看集合中是否包含满足条件的数据
    def check_exist(self, query):
        ret = self.table.find_one(query)
        return ret is not None

    # 如果没有则新建
    def update(self, query, kv_dict):
        self.table.update_one(query, {
            '$set': kv_dict
        }, upsert=True)
