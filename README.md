# Dataset

This repository is a fork from https://github.com/greenelab/model-free-data/ in order to make a subset of dataset compatible with Orange. 
It introduces Orange  metadata inside each of the datasets and change the extension to  `.tab`. 
for mor informatio about the dataset refer to https://github.com/greenelab/model-free-data/blob/master/README.md

# Migration Script

Inside is also the migration script, it can be re-run in order to generate again the Orange-compatible datasets. 
The script can be execute with `python ./migrate.py`