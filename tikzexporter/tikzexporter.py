from yaramo.model import Topology

class TikZExporter:

    @staticmethod
    def export(
            topology: Topology, target_filename: str = None,
            x_scale_factor: float = 1.0,
            y_scale_factor: float = 1.0,
            node_class: str = "",
            node_style: str = "",
            edge_class: str = "",
            edge_style: str = "",
        ):
        node_str = TikZExporter._get_node_str(topology, x_scale_factor, y_scale_factor, node_class)
        edge_str = TikZExporter._get_edge_str(topology, x_scale_factor, y_scale_factor, edge_class)
        TikZExporter._print_result(target_filename, node_str, edge_str, node_style, edge_style)

    @staticmethod
    def _get_node_str(topology: Topology, x_scale_factor: float, y_scale_factor: float, node_class: str):
        node_str = ""
        classes = "yaramonode"
        if node_class:
            classes += f", {node_class}"
        for node in topology.nodes.values():
            x = node.geo_node.x * x_scale_factor
            y = node.geo_node.y * y_scale_factor
            ident = TikZExporter._uuid_to_identifier(node.uuid)
            node_str += f"\t\\node[{classes}] ({ident}) at({x},{y}) {{}};\n"
        return node_str

    @staticmethod
    def _get_edge_str(topology: Topology, x_scale_factor: float, y_scale_factor: float, edge_class: str):
        edge_str = ""
        classes = "yaramoedge"
        if edge_class:
            classes += f", {edge_class}"
        for edge in topology.edges.values():
            a_ident = TikZExporter._uuid_to_identifier(edge.node_a.uuid)
            b_ident = TikZExporter._uuid_to_identifier(edge.node_b.uuid)
            inter_geo_nodes_str = ""
            for inter_geo_node in edge.intermediate_geo_nodes:
                x = inter_geo_node.x * x_scale_factor
                y = inter_geo_node.y * y_scale_factor
                inter_geo_nodes_str += f" ({x},{y}) --"
            edge_str += f"\t\\draw[{classes}] ({a_ident}) --{inter_geo_nodes_str} ({b_ident});\n"
        return edge_str

    @staticmethod
    def _uuid_to_identifier(uuid):
        return uuid[-5:]

    @staticmethod
    def _print_result(target_filename: str, node_str: str, edge_str: str, node_style: str, edge_style: str):
        result_str = f"""\\begin{{tikzpicture}}[yaramonode/.style={{{node_style}}}, yaramoedge/.style={{{edge_style}}}]
{node_str}
{edge_str}
\\end{{tikzpicture}}
"""
        if target_filename is None:
            print(result_str)
        else:
            with open(target_filename, "w", encoding="utf-8") as file:
                file.write(result_str)
