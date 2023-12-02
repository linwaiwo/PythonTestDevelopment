def pytest_collection_modify_items(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识node_id的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._node_id = i.node_id.encode("utf-8").decode("unicode_escape")
