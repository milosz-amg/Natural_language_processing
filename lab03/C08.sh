#!/bin/bash
tr -d '[:punct:]' < interp.in > interp.out
wc -w < interp.out