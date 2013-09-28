DROP TABLE IF EXISTS gdelt_rcfiletest;
SET hive.exec.compress.output=true;
SET mapred.max.split.size=256000000;
SET mapred.output.compression.type=BLOCK;
SET mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec;
CREATE TABLE gdelt_rcfiletest LIKE gdelt STORED AS RCFILE;
INSERT OVERWRITE gdelt_rcfiletest SELECT * FROM gdelt;


