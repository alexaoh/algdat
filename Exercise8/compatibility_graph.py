def compatibility_graph(donors, recipients, k):
    donor_edges = []
    for donor in range(len(donors)):
        donor_edges.append([])
        for recipient in range(len(recipients)):
            count = 0
            for att in range(len(recipients[recipient])):
                if donors[donor][att] == recipients[recipient][att]:
                    count += 1
            if count >= k:
                donor_edges[donor].append(recipient)

    return donor_edges

