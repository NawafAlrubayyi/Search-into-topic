# Search-into-topic

1- kafka-cli.py script will produce the content of Sample10CSVFile_2kb.csv file.
2- read-store.py script will consume the topic event and put them in output.txt file.
3- search.py script will search for specific value in output.txt file and print the whole event that have this value as a part of it.


to run search.py you should open terminal and type the following:

D:\Program Files\Python-kafka-Cli-main\Python-kafka-Cli-main> python search.py output.txt {"your_search_value"}

replace your_search_value with the value that you want to search for
