import networkx as nx
import matplotlib.pyplot as plt
from slackConnector import slackConnector

def main():
    #connect the database
    connector = slackConnector('Slack analysis')

    user_helper = connector.select_user_helper()
    parent_child = connector.select_parent_child()
    connector.close_database()

    # G = mentions_net_work(user_helper)
    # pos=nx.spring_layout(G)

    # print(center_node(pos))
    # order_dict = order_node(user_helper)
    # print(order_dict)

    # print("order by time been helped:")
    # print(sorted(order_dict.items(), key = lambda item: item[1][0]))

    # print("order by time helped others:")
    # help_order = sorted(order_dict.items(), key = lambda item: item[1][1])

    # print("order by active:")
    # print(sorted(order_dict.items(), key = lambda item: item[1][1] + item[1][0]))

    # node_order_dict = sorted(order_dict.items(), key = lambda item: item[0])

    # size = [value[1] for node, value in node_order_dict]

    # nx.draw(G, pos = pos, with_labels = True, node_size = [30 * item for item in size], alpha = 0.6)
    # blue_node = help_order[-10:]
    # nx.draw_networkx_nodes(G, pos = pos, nodelist = [node for node, value in blue_node], node_color = 'b', node_size = [30 * value[1] for node, value in blue_node], alpha = 0.6)
    
    # plt.show()

    
    weighted_records, id_replies = weighted_relation(parent_child)
    G = replies_net_work(weighted_records)

    pos=nx.spring_layout(G)
    weight_list = [weight for u, v, weight in G.edges(data=True)]

    print(id_replies)

    #print(weighted_records)

    #ordered_weight_list = sorted(weighted_records.items(), key = lambda item: item[1])
    #print(ordered_weight_list)

    node_list = G.nodes
    print(len(node_list))
    print(len(id_replies))
    size_list = []
    for node in node_list:
        if node in id_replies:
            size_list.append(id_replies[node] * 100)
        else:
            size_list.append(100)

    nx.draw(G, pos = pos, node_color='#A0CBE2', node_size = size_list, edge_color = [dict['weight'] for dict in weight_list], width=4, edge_cmap=plt.cm.Blues, with_labels = True, alpha = 0.8)
    #nx.draw_networkx_edges(G, pos=pos, edgelist=[edge for edge, weight in ordered_weight_list] , edge_color = [weight for edge, weight in ordered_weight_list], width=4, edge_cmap=plt.cm.Blues, alpha = 0.8)

    plt.show()

def mentions_net_work(user_helper):
    G = nx.DiGraph()
    id_set = set()
    
    for user, helper in user_helper:
        id_set.add(helper)
        id_set.add(user)

    for node in id_set:
        G.add_node(node)

    for user, helper in user_helper:
        G.add_edge(user, helper)

    return G

def center_node(pos):

    cent = 10

    for node in pos:
        node_pos = abs(pos[node][0]) + abs(pos[node][1])
        if node_pos < cent:
            cent = node_pos
            center = node

    return center

def order_node(user_helper):
    # order_dict = {id: [time been helped, time help others]}
    order_dict = {}

    for user, helper in user_helper:
        if user not in order_dict:
            order_dict[user] = [0, 0]
        if helper not in order_dict:
            order_dict[helper] = [0, 0]

        order_dict[user][0] += 1
        order_dict[helper][1] += 1

    return order_dict

def replies_net_work(weighted_record):
    G = nx.Graph()
    for parent, child in weighted_record:
        G.add_edge(parent, child, weight=weighted_record[(parent, child)])

    return G

def weighted_relation(replies_record):
    weighted_record = {}
    id_replies = {}
    for parent, child in replies_record:
        if (parent, child) not in weighted_record or (child, parent) not in weighted_record:
            weighted_record[(parent, child)] = 1
        elif (parent, child) in weighted_record:
            weighted_record[(parent, child)] += 1
        elif (child, parent) in weighted_record:
            weighted_record[(child, parent)] += 1

        if parent not in id_replies:
            id_replies[parent] = 0
        
        id_replies[parent] += 1
        
    return weighted_record, id_replies


if __name__ == "__main__":
    main()