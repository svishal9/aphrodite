#!/bin/bash

set -euo pipefail


function trace() {
    {
        local tracing
        [[ "$-" = *"x"* ]] && tracing=true || tracing=false
        set +x
    } 2>/dev/null
    if [ "$tracing" != true ]; then
        # Bash's own trace mode is off, so explicitely write the message.
        echo "$@" >&2
    else
        # Restore trace
        set -x
    fi
}


function contains () {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}


# Parse arguments.
operations=()
subcommand_opts=()
while true; do
    case "${1:-}" in
    setup)
        operations+=( setup )
        shift
        ;;
    lint|linting)
        operations+=( linting )
        shift
        ;;
    tests)
        operations+=( tests )
        shift
        ;;
    docker-tests)
        operations+=( docker-tests )
        shift
        ;;
    docker-run)
        operations+=( docker-run )
        shift
        ;;
    start-postgres)
        operations+=( start-postgres )
        shift
        ;;
    stop-postgres)
      operations+=( stop-postgres )
      shift
      ;;
    connect-to-local-postgres)
        operations+=( connect-to-local-postgres )
        shift
        ;;
    run)
        operations+=( run )
        shift
        ;;
    --)
        shift
        break
        ;;
    -h|--help)
        operations+=( usage )
        shift
        ;;
    *)
        break
        ;;
    esac
done
if [ "${#operations[@]}" -eq 0 ]; then
    operations=( usage )
fi
if [ "$#" -gt 0 ]; then
    subcommand_opts=( "$@" )
fi


function usage() {
    trace "$0 <command> [--] [options ...]"
    trace "Commands:"
    trace "    linting   Static analysis, code style, etc."
    trace "    precommit Run sensible checks before committing"
    trace "    run       Run the application"
    trace "    setup     Install dependencies"
    trace "    tests     Run tests"
    trace "    docker-tests     Run tests in docker"
    trace "    docker-run     Run app in docker"
    trace "    start-postgres     Start Postgres"
    trace "    stop-postgres     Stop Postgres"
    trace "    connect-to-local-postgres     Connect to local Postgres"
    trace "Options are passed through to the sub-command."
}


function setup() {
    trace "Setting up"
    ./scripts/setup.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}


function linting() {
    trace "Linting"
    ./scripts/linting.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}


function tests() {
    trace "Running tests"
    ./scripts/run_tests.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}


function docker-tests() {
    trace "Running tests in docker container"
    ./scripts/docker-tests.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}

function docker-run() {
    trace "Running application in docker container"
    ./scripts/docker-run.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}





function start-postgres() {
    trace "Start Postgres docker container"
    ./scripts/start-postgres.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}


function stop-postgres() {
    trace "Start Postgres docker container"
    ./scripts/stop-postgres.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}

function connect-to-local-postgres() {
    trace "Connect to local Postgres"
    ./scripts/connect-to-local-postgres.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}


function run() {
    trace "Running app"
    ./scripts/run-app.sh "${subcommand_opts[@]:+${subcommand_opts[@]}}"
}


script_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "${script_directory}/"


if contains usage "${operations[@]}"; then
    usage
    exit 1
fi
if contains setup "${operations[@]}"; then
    setup
fi
if contains linting "${operations[@]}"; then
    linting
fi
if contains tests "${operations[@]}"; then
    tests
fi
if contains docker-tests "${operations[@]}"; then
    docker-tests
fi
if contains docker-run "${operations[@]}"; then
    docker-run
fi
if contains start-postgres "${operations[@]}"; then
    start-postgres
fi
if contains stop-postgres "${operations[@]}"; then
    stop-postgres
fi
if contains connect-to-local-postgres "${operations[@]}"; then
    connect-to-local-postgres
fi
if contains run "${operations[@]}"; then
    run
fi


trace "Exited cleanly."
