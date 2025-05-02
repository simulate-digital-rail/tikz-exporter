from yaramo.model import Topology, Node, DbrefGeoNode, Edge
from tikzexporter import TikZExporter


def simple_test():
    topology = Topology()
    node_1 = Node(geo_node=DbrefGeoNode(0, 5))
    node_2 = Node(geo_node=DbrefGeoNode(0, 0))
    node_3 = Node(geo_node=DbrefGeoNode(10, 0))  # Point
    node_4 = Node(geo_node=DbrefGeoNode(20, 0))  # Point
    node_5 = Node(geo_node=DbrefGeoNode(27, 5))
    node_6 = Node(geo_node=DbrefGeoNode(30, 0))  # Point
    node_7 = Node(geo_node=DbrefGeoNode(40, 0))  # Point
    node_8 = Node(geo_node=DbrefGeoNode(50, 0))  # Point
    node_9 = Node(geo_node=DbrefGeoNode(60, 5))
    node_10 = Node(geo_node=DbrefGeoNode(60, 0))
    edge_1 = Edge(node_1, node_3, intermediate_geo_nodes=[DbrefGeoNode(7.5, 5)])
    edge_2 = Edge(node_2, node_3)
    edge_3 = Edge(node_4, node_3)
    edge_4 = Edge(node_4, node_5, intermediate_geo_nodes=[DbrefGeoNode(22.5, 5)])
    edge_5 = Edge(node_4, node_6)
    edge_6 = Edge(node_7, node_6)
    edge_7 = Edge(
        node_6, node_7, intermediate_geo_nodes=[DbrefGeoNode(32.5, 5), DbrefGeoNode(37.5, 5)]
    )
    edge_8 = Edge(node_8, node_7)
    edge_9 = Edge(node_8, node_9, intermediate_geo_nodes=[DbrefGeoNode(52.5, 5)])
    edge_10 = Edge(node_8, node_10)
    topology.add_nodes(
        [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10]
    )
    topology.add_edges(
        [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7, edge_8, edge_9, edge_10]
    )

    TikZExporter.export(
        topology,
        x_scale_factor=0.2,
        y_scale_factor=0.1,
        y_shift=-2.0,
        node_class="",
        node_style="circle, draw, fill=black,inner sep=0pt,minimum size=6pt",
        edge_class="schemutrack",
        edge_style=""
    )


if __name__ == "__main__":
    simple_test()