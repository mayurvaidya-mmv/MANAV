from research.topic_normalizer import TopicNormalizer


queries = [

    "Research MQTT",

    "Research mqtt",

    "Research MQTT Protocol",

    "Research Message Queuing Telemetry Transport",

    "Research UDP",

    "Research User Datagram Protocol",

    "Research Modbus",

    "Research Modbus TCP",

    "Research RS-485",

]

for query in queries:

    print(

        f"{query:50}",

        "->",

        TopicNormalizer.normalize(query)

    )