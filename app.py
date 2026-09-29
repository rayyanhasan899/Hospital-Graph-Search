import streamlit as st
import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt

from searchAlgos import (
    hospital_graph,
    locations,
    gbfs,
    a_star
)


# Streamlit GUI
#*******************#

# Set Page Config

st.set_page_config(
    page_title="Hospital Search Visualization",
    page_icon="🏥",
    layout="wide"
)

# Meaningful title and description

st.title("Hospital Emergency Supply Search")
st.write(
    "Interactive visualization of Greedy Best-First Search (GBFS) "
    "and A* Search on the hospital weighted graph."
)

# Define the nodes and their coordinates

nodes = list(hospital_graph.keys())

# Create selectboxes for initial and goal nodes

start = st.selectbox(
    "Select Initial Node",
    nodes,
    index=nodes.index("Pharmacy")
)

goal = st.selectbox(
    "Select Goal Node",
    nodes,
    index=nodes.index("Emergency_Ward")
)

# Create a selectbox for the search algorithm

algorithm = st.selectbox(
    "Select Search Algorithm",
    ["GBFS", "A*"]
)

if st.button("Run Search"):

    if algorithm == "GBFS":

        path, cost = gbfs(start, goal)

    else:

        path, cost = a_star(start, goal)

    if path is None:

        st.error("No path was found between the selected nodes.")

    else:

        # Display result

        st.subheader("Search Result")

        st.write(
            f"**Algorithm:** {algorithm}"
        )

        st.write(
            f"**Solution Path:** {' → '.join(path)}"
        )

        st.write(
            f"**Total Path Cost:** {cost:.2f}"
        )

        # Visualize NetworkX graph

        G = nx.DiGraph()

        for node, neighbors in hospital_graph.items():

            G.add_node(
                node,
                pos=locations[node]
            )

            for neighbor, weight in neighbors.items():

                G.add_edge(
                    node,
                    neighbor,
                    weight=weight
                )

        pos = locations

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        nx.draw_networkx_nodes(
            G,
            pos,
            ax=ax,
            node_size=2200
        )

        nx.draw_networkx_edges(
            G,
            pos,
            ax=ax,
            arrows=True,
            arrowsize=20
        )

        nx.draw_networkx_labels(
            G,
            pos,
            ax=ax,
            font_size=9
        )

        edge_labels = nx.get_edge_attributes(
            G,
            "weight"
        )

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=edge_labels,
            ax=ax
        )

        solution_edges = list(
            zip(path, path[1:])
        )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=solution_edges,
            ax=ax,
            width=4,
            arrows=True,
            arrowsize=22
        )

        ax.set_title(
            f"{algorithm} Solution Path"
        )

        ax.axis("off")

        st.pyplot(fig)
