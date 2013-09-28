
# Protobuf 

Use OpenStreetMap pbf format as a model 

http://wiki.openstreetmap.org/wiki/PBF_Format

Keep first revision simple 

## Goals 

Versioned 
Easily splittable in Hadoop ingestion
Works with multiple languages
Easily imported into Hive or Impala

## Installation 

brew install protobuf
brew install snappy 
pip install python-snappy
pip install protobuf 

protoc --python_out=. gdelt.proto









