Como rodar kafka:

instalar jdk 8

Rodar cluster:
.\bin\windows\zookeeper-server-start.bat config\zookeeper.properties

.\bin\windows\kafka-server-start.bat config\server.properties

Testar cluster:
Criar tópico para enviar mensagens:
.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

Abrir dois powershell e rodar os seguintes comandos:
Iniciar consumidor:
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning


Iniciar produtor:
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic test
Após é só escrever na linha de comando shell na tela do produtor e a mensagem vai aparecer no consumidor