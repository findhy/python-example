#����Mapper
cat *.log | python ad_static_mapper.py

#����Mapper��Reducer
cat *.log | python ad_static_mapper.py | sort -k1,1 | python ad_static_reducer.py