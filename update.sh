#!/usr/bin/env bash
git pull
./joplinexport.py
git add .
git diff --cached
git cma Updates
