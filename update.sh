#!/usr/bin/env bash
./joplinexport.py
git add .
git diff --cached
