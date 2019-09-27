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
CLIENT_DIR="$DIR/../../aegisblade/clients/python"


function run_example_test {
  example_name="$1"

  if [ ! -d "$DIR/$example_name/venv" ]; then
    virtualenv "$DIR/$example_name/venv"
  fi

  source "$DIR/$example_name/venv/bin/activate"

  pip install --upgrade "$CLIENT_DIR"

  (cd "$DIR/$example_name" && pip install -r ./requirements.txt && python -u ./main.py)
}


function run_example {
  example_name="$1"

  if [ ! -d "$DIR/$example_name/venv" ]; then
    virtualenv "$DIR/$example_name/venv"
  fi

  source "$DIR/$example_name/venv/bin/activate"

  (cd "$DIR/$example_name" && pip install -r ./requirements.txt && python -u ./main.py)
}


if [ "$MODE" == "test" || -z "$MODE" ]; then
  export AEGISBLADE_LIBRARIES="aegisblade=$CLIENT_DIR"
  export AEGISBLADE_VERIFY_SSL=false

  run_example_test helloworld
  run_example_test selenium
  run_example_test local_library

elif [ "$MODE" == "prod" ]; then
  
  run_example helloworld
  run_example selenium
  run_example local_library

fi
