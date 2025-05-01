from yaramo.model import Topology

class TikZExporter:

    @staticmethod
    def export(
            topology: Topology, target_filename: str = None,
            scale_factor: float = 1,
            node_style: str = "",
            edge_style: str = ""
        ):
        node_str = TikZExporter._get_node_str(topology, scale_factor)
        edge_str = TikZExporter._get_edge_str(topology)
        TikZExporter._print_result(target_filename, node_str, edge_str, node_style, edge_style)

    @staticmethod
    def _get_node_str(topology, scale_factor):
        node_str = ""
        for node in topology.nodes.values():
            x = node.geo_node.x * scale_factor
            y = node.geo_node.y * scale_factor
            ident = TikZExporter._uuid_to_identifier(node.uuid)
            node_str += f"\t\\node[yaramonode] ({ident}) at({x},{y}) {{}};\n"
        return node_str

    @staticmethod
    def _get_edge_str(topology):
        edge_str = ""
        for edge in topology.edges.values():
            a_ident = TikZExporter._uuid_to_identifier(edge.node_a.uuid)
            b_ident = TikZExporter._uuid_to_identifier(edge.node_b.uuid)
            edge_str += f"\t\\draw[yaramoedge] ({a_ident}) -- ({b_ident});\n"
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