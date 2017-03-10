#!/usr/bin/env bash

if [ $1 = 'startdebug' ]; then
    gunicorn --reload ZKTeam.wsgi:application --bind 0.0.0.0:8083
elif [ $1 = 'start' ]; then
    nohup gunicorn --reload ZKTeam.wsgi:application --bind 0.0.0.0:8083 &
elif [ $1 = 'stop' ]; then
    ps aux  |  grep -i ZKTeam.wsgi:application  |  awk '{print $2}'  |  xargs sudo kill -9
elif [ $1 = 'restart' ]; then
    ps aux  |  grep -i JSMocker.wsgi:application  |  awk '{print $2}'  |  xargs sudo kill -9
    nohup gunicorn --reload ZKTeam.wsgi:application --bind 0.0.0.0:8082 &
fi
