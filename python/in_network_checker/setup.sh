#!/usr/bin/env bash
# setup.sh
# Configures a python 2.7 virtual environment for Jupyter Notebooks
rm -rf venv
virtualenv venv
source venv/bin/activate && pip install -r requirements.txt
