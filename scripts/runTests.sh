#!/bin/bash
if [ $# -ne 1 ]
then
    1>&2 "Invalid number of arguments."
    exit 1
fi

runFile=$1.py # Currently only runs Python tests
testFile=test/$1/list
if [ ! -x ${runFile} ]
then
    1>&2 "Input problem is not runnable or does not exist."
    exit 1
elif [ ! -r ${testFile} ]
then
    1>&2 "Test 'list' file is not readable or does not exist."
    exit 1
fi

tests=$(cat ${testFile})
for test in $tests
do
    newOutputFile=$(mktemp)
    givenOutputFile=test/$1/${test}.out
    if [ ! -r $givenOutputFile ]
    then
        1>&2 "Output file ${givenOutputFile} is not readable or does not exist."
        exit 1
    fi

    inputFile=test/$1/${test}.in
    if [ -r $inputFile ]
    then
        python $runFile < $inputFile > $newOutputFile
    else
        python $runFile > $newOutputFile
    fi
    diff $newOutputFile $givenOutputFile > /dev/null

    if [ $? -ne 0 ]
    then
        echo "Test failed: ${test}"
        echo "Expected:"
        cat $givenOutputFile
        echo
        echo "Actual:"
        cat $newOutputFile
        exit 1
    fi
    rm $newOutputFile
done
exit 0
