from SRC.common import xmlHelper

tree=xmlHelper.read_xml('uShop.xml')
connection_node=xmlHelper.find_nodes(tree,'connection')
hub_nodes=xmlHelper.find_nodes(connection_node[0],'hub1')



node=xmlHelper.get_node_by_keyvalue(hub_nodes,{'enabled':'True'})
i=1


# res=xmlHelper.if_match(nodes_scene[0],{'schemeId':'0'})
# print(res)