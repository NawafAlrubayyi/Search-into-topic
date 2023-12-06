import subprocess

def run_kafka_consumer():
    # Command to run the Kafka Avro console consumer

    command = [
        "docker", "exec", "-i", "kafka-cli",
        "kafka-avro-console-consumer",
        "--bootstrap-server", "broker:9093",
        "--topic", "AKFK-21",
        "--property", "value.schema.id=2",
        "--property", "schema.registry.url=http://schema-registry:8081",
        "--from-beginning",
        "--timeout-ms", "5000"
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("Output:", output.decode('utf-8'))
    msgs = output.decode().splitlines()[64:-4]
    with open("output.txt", "a") as f:
        for msg in msgs:
            print(msg, file=f)

run_kafka_consumer()