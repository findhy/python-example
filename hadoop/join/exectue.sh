#����Mapper
cat *.log | python ad_static_mapper.py

#����Mapper��Reducer
cat *.log | python ad_static_mapper.py | sort -k1,1 | python ad_static_reducer.py

#Hadoop��Ⱥ����
hadoop jar /home/hadoop/hadoop-2.0.0-cdh4.3.2/share/hadoop/tools/lib/hadoop-streaming-2.0.0-cdh4.3.2.jar -input /ad/log/*/* -output /ad/static_detail_output -file ./ad_static*.py -mapper "python ad_static_mapper.py" -reducer "python ad_static_reducer.py"