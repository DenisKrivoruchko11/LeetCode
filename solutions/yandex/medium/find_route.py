def get_route(tickets):
    src_to_index = {}
    trg = set()
    for i, ticket in enumerate(tickets):
        src_to_index[ticket['from']] = i
        trg.add(ticket['to'])

    index = -1
    for v in src_to_index:
        if v not in trg:
            index = src_to_index[v]
            break

    result = []
    while True:
        result.append(tickets[index])
        if len(result) == len(tickets):
            return result
        index = src_to_index[tickets[index]['to']]