#!/bin/bash

rm -rf "$PWD"/reports/allure
rm -rf "$PWD"/csv

pytest --alluredir="$PWD"/reports/allure

allure serve "$PWD"/reports/allure