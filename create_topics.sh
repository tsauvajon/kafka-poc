kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 5 --topic new_image
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 5 --topic image_ready
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 5 --topic metrics_extracted
