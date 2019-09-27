#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ "$SOURCE" != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

set -e

MODE="$1"
CLIENT_DIR="$DIR/../../aegisblade/clients/nodejs"

function run_example_test {
  example_name="$1"

  (cd "$DIR/$example_name" && npm install && npm install "$CLIENT_DIR" && node main.js)
}

function run_example {
  example_name="$1"

  (cd "$DIR/$example_name" && npm install && node main.js)
}

if [ "$MODE" == "test" || -z "$MODE" ]; then

  export AEGISBLADE_LIBRARIES="$CLIENT_DIR"
  export AEGISBLADE_VERIFY_SSL=false

  run_example_test helloworld
  run_example_test local_library/my_application
  run_example_test puppeteer
  run_example_test puppeteer-chrome

elif [ "$MODE" == "prod" ]; then 

  run_example helloworld
  run_example local_library/my_application
  run_example puppeteer
  run_example puppeteer-chrome

fi