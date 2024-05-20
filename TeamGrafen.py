from graphviz import Digraph

def main():
    
    edges = [
        ('Sebastian', 'Victor'),
        ('Victor', 'Sebastian'),
        ('Victor', 'Joachim'),
        ('Joachim', 'Victor'),
        ('Sebastian', 'Jonas'),
        ('Jonas', 'Sebastian'),
        ('Kaja', 'Mari'),
        ('Mari', 'Kaja')
    ]

    
    strongly_connected_components = [
        {'Sebastian', 'Victor'},
        {'Kaja', 'Mari'},
        {'Jonas', 'Sebastian'},
        {'Joachim', 'Victor'}
    ]

    
    dot = Digraph(comment='Sterkt sammenhengende komponenter', format='svg')

    
    for start_node, end_node in edges:
        dot.edge(start_node, end_node)

    
    for i, component in enumerate(strongly_connected_components):
        with dot.subgraph(name='cluster_{}'.format(i)) as c:
            c.attr(color='white')
            for node in component:
                c.node(node)

    
    dot.render('graph_scc')

    
    print(dot.source)


if __name__ == "__main__":
    main()