#!/bin/bash

rm -rf "$PWD"/reports/allure

pytest --alluredir="$PWD"/reports/allure

allure serve "$PWD"/reports/allure