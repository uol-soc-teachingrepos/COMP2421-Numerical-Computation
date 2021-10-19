#!/bin/bash

diff ${1} <(pandoc ${1} -s -t markdown --wrap=none)
