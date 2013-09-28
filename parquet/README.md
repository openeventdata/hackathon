# Parquet


## Use Parquet with Snappy Compression to improve query speed. 

## Full example 

https://github.com/tlpinney/funnelcloud/tree/master/clouds/gdelt

Spot pricing is unstable this weekend. Use normal ec2 instances for now.


## Requirements 

CDH4 that supports Parquet 

## Installation 

Download csv files to a cluster 

    hdfs dfs -mkdir gdelt_historical_tsv 
    for i in `cat /home/ubuntu/backfiles.txt`; do
      curl -O http://gdelt.utdallas.edu/data/backfiles/$i.zip
      unzip $i.zip
      # no headers
      # tail -n +2 $i.csv > $i.tmp 
      # mv $i.tmp $i.csv 
      hdfs dfs -put $i.csv gdelt_historical_tsv 
    done 

    hdfs dfs -mkdir gdelt_dailyupdates_tsv 
    for i in `cat /home/ubuntu/dailyupdates.txt`; do 
      curl -O http://gdelt.utdallas.edu/data/dailyupdates/$i.zip 
      unzip $i.zip
      # no headers 
      # tail -n +2 $i > $i.tmp 
      # mv $i.tmp $i 
      hdfs dfs -put $i gdelt_dailyupdates_tsv 
    done

    # run the sql create table and ingestion 
    
    impala-shell -i localhost < create_gdelt.sql

     





