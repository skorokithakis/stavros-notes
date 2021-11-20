#!/usr/bin/env bash
git pull
./joplinexport
git add .
git diff --cached
git cma Updates
