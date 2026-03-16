from property_data import properties


def recommend_property(query):

    query = query.lower()

    results = []

    if "2 bedroom" in query or "2 bed" in query:

        for p in properties:
            if p["bedrooms"] == 2:
                results.append(p)

    elif "villa" in query:

        for p in properties:
            if p["type"] == "villa":
                results.append(p)

    else:
        results = properties[:2]

    return results